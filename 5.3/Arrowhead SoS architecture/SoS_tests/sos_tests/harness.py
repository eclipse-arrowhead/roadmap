"""HTTPS-only, certificate-verifying fixture executor and observable test oracles.

No implementation is simulated here. Missing live fixtures raise SkipTest.
"""
from pathlib import Path
import datetime as dt,json,os,re,ssl,unittest,urllib.error,urllib.parse,urllib.request

class ConfigurationError(ValueError):pass
class MissingFixture(unittest.SkipTest):pass

def pointer(value,path):
    if path=='':return value
    if not isinstance(path,str) or not path.startswith('/'):raise ConfigurationError('JSON pointer must be empty or start with /')
    for part in path[1:].split('/'):
        key=part.replace('~1','/').replace('~0','~')
        try:value=value[int(key)] if isinstance(value,list) else value[key]
        except (KeyError,IndexError,ValueError,TypeError) as e:raise AssertionError('Missing response pointer '+path) from e
    return value

def render(value,variables,_seen=frozenset()):
    if isinstance(value,dict):return {k:render(v,variables,_seen) for k,v in value.items()}
    if isinstance(value,list):return [render(v,variables,_seen) for v in value]
    if not isinstance(value,str):return value
    def get(name):
        if name.startswith('url:'):return urllib.parse.quote(str(get(name[4:])),safe='')
        if name not in variables:raise MissingFixture('Missing fixture variable '+name)
        if name in _seen:raise ConfigurationError('Cyclic fixture variable '+name)
        return render(variables[name],variables,_seen|{name})
    match=re.fullmatch(r'\$\{([^}]+)\}',value)
    if match:return get(match[1])
    return re.sub(r'\$\{([^}]+)\}',lambda m:str(get(m[1])),value)

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):raise ConfigurationError('Redirect refused; configure the exact protected endpoint')

class HTTPS:
    def __init__(self,profile,base_dir):self.profile=profile;self.base_dir=Path(base_dir)
    def path(self,v):
        p=Path(os.path.expandvars(v));return str(p if p.is_absolute() else self.base_dir/p)
    def request(self,recipe,variables):
        recipe=render(recipe,variables)
        endpoint=recipe['endpoint'];origin=self.profile.get('endpoints',{}).get(endpoint)
        if not origin:raise MissingFixture('Missing HTTPS endpoint '+endpoint)
        parts=urllib.parse.urlsplit(origin)
        if parts.scheme!='https' or not parts.hostname or parts.username or parts.password or parts.query or parts.fragment:raise ConfigurationError('Endpoint must be an HTTPS origin without credentials/query/fragment')
        path=recipe['path']
        if not path.startswith('/') or path.startswith('//'):raise ConfigurationError('Request path must be origin-relative')
        url=origin.rstrip('/')+path
        if recipe.get('query'):url+='?'+urllib.parse.urlencode(recipe['query'],doseq=True)
        actor=self.profile.get('actors',{}).get(recipe.get('actor','inspector'))
        if actor is None:raise MissingFixture('Missing actor '+recipe.get('actor','inspector'))
        ca=self.profile.get('ca')
        if not ca:raise MissingFixture('Missing trusted cloud CA')
        context=ssl.create_default_context(cafile=self.path(ca));context.minimum_version=ssl.TLSVersion.TLSv1_2
        if actor.get('cert'):
            if not actor.get('key'):raise ConfigurationError('Actor certificate needs its key')
            context.load_cert_chain(self.path(actor['cert']),self.path(actor['key']))
        headers={'Content-Type':'application/json'}
        envname=actor.get('token_env')
        if envname:
            token=os.environ.get(envname)
            if not token:raise MissingFixture('Missing token environment variable '+envname)
            headers['Authorization']='Bearer IDENTITY-TOKEN//'+token
        for k,v in recipe.get('headers',{}).items():
            if k.lower()=='authorization':raise ConfigurationError('Supply tokens through actor token_env, not fixture text')
            headers[k]=str(v)
        body=json.dumps(recipe['body']).encode() if 'body' in recipe else None
        req=urllib.request.Request(url,data=body,headers=headers,method=recipe.get('method','GET'))
        opener=urllib.request.build_opener(NoRedirect(),urllib.request.HTTPSHandler(context=context))
        try:
            with opener.open(req,timeout=self.profile.get('timeout_seconds',15)) as response:
                raw=response.read(8*1024*1024+1);status=response.status
        except urllib.error.HTTPError as e:raw=e.read(8*1024*1024+1);status=e.code
        except (ssl.SSLError,urllib.error.URLError) as e:
            reason=getattr(e,'reason',e)
            # Connection refused, timeouts and DNS failure are not proof of TLS rejection.
            if isinstance(reason,ssl.SSLError) and (isinstance(reason,ssl.SSLCertVerificationError) or any(tag in str(reason).upper() for tag in ['CERTIFICATE_REQUIRED','CERTIFICATE_VERIFY_FAILED','BAD_CERTIFICATE','CERTIFICATE_REVOKED','UNKNOWN_CA','ALERT_ACCESS_DENIED'])):return {'status':None,'body':None,'tls_rejected':True}
            raise
        if len(raw)>8*1024*1024:raise AssertionError('Response exceeds fixture runner limit')
        try:body=json.loads(raw) if raw else None
        except (ValueError,UnicodeError):body=raw.decode(errors='replace')
        return {'status':status,'body':body,'tls_rejected':False}

DENIAL={'denied':{401,403},'client_error':set(range(400,500)),'denied_or_unavailable':{401,403,503},'denied_or_not_found':{401,403,404,410}}

def assert_oracle(test,case,response,observed,expected=None):
    p=case['predicate']
    if p=='tls_rejected':test.assertTrue(response.get('tls_rejected'),case['title']);return
    test.assertFalse(response.get('tls_rejected'), 'TLS failed before the behavior could be observed')
    if p in DENIAL:test.assertIn(response['status'],DENIAL[p]);return
    test.assertIn(response['status'],range(200,300),'Expected successful observation request')
    if p=='equals':
        if isinstance(expected,bool):test.assertIsInstance(observed,bool)
        test.assertEqual(observed,expected)
    elif p=='not_equals':test.assertNotEqual(observed,expected)
    elif p=='empty':test.assertIsInstance(observed,(list,dict,str));test.assertEqual(len(observed),0)
    elif p=='nonempty':test.assertIsInstance(observed,(list,dict,str));test.assertGreater(len(observed),0)
    elif p=='contains':test.assertIn(expected,observed)
    elif p=='not_contains':test.assertNotIn(expected,observed)
    elif p=='length_at_most':test.assertIsInstance(observed,(list,dict,str));test.assertLessEqual(len(observed),expected)
    elif p=='subset':test.assertIsInstance(observed,list);test.assertIsInstance(expected,list);test.assertTrue(all(v in expected for v in observed))
    elif p=='one_of':test.assertIn(observed,expected)
    elif p=='telemetry':
        test.assertIsInstance(observed,dict)
        for key in ['provider','observationType','sourceTime','sequence','value','unit','quality']:test.assertIn(key,observed)
        test.assertEqual(observed['provider'],expected);test.assertIn(observed['observationType'],['echo','power','status'])
        test.assertIsInstance(observed['sequence'],int);test.assertNotIsInstance(observed['sequence'],bool);test.assertGreaterEqual(observed['sequence'],0)
        stamp=dt.datetime.fromisoformat(observed['sourceTime'].replace('Z','+00:00'));test.assertIsNotNone(stamp.tzinfo)
        test.assertIsInstance(observed['quality'],str);test.assertTrue(observed['quality'])
    else:raise ConfigurationError('Unknown oracle '+p)

def write_required(recipe):
    method=recipe.get('method','GET').upper()
    if method in ['GET','HEAD','OPTIONS']:return False
    path=recipe.get('path','').rstrip('/')
    return not (method=='POST' and path.split('/')[-1] in ['lookup','query','verify','check','logs','query-alarms'])

class Executor:
    def __init__(self,profile,base_dir,allow_mutations=False,transport=None):
        self.profile=profile;self.allow_mutations=allow_mutations;self.transport=transport or HTTPS(profile,base_dir)
    def execute(self,test,case):
        f=self.profile.get('scenarios',{}).get(case['id'])
        if f is None:raise MissingFixture('No isolated live fixture for '+case['id'])
        if not self.profile.get('test_environment'):raise ConfigurationError('Live tests require an explicitly configured test_environment')
        variables=dict(self.profile.get('variables',{}));variables.update(f.get('variables',{}))
        for name,envname in self.profile.get('secret_variables',{}).items():
            if envname in os.environ:variables[name]=os.environ[envname]
        negative=case['predicate'] in DENIAL or case['predicate']=='tls_rejected'
        if negative and 'control' not in f:raise MissingFixture('Negative case needs a successful control request for the protected operation')
        recipes=[*([f['control']] if 'control' in f else []),*f.get('setup',[]),f['request'],*f.get('cleanup',[])]
        if any(write_required(r) for r in recipes) and not(self.allow_mutations and self.profile.get('isolated')):raise MissingFixture('Mutating scenario needs --allow-mutations and isolated=true')
        # Resolve all declared static inputs before side effects. Captured values are
        # allowed only after their producing step, so setup cannot partially execute
        # merely because an unrelated later variable is missing.
        known=dict(variables)
        for recipe in recipes:
            render(recipe,known)
            for name in recipe.get('capture',{}):known[name]='<captured>'
        render(case.get('expected'),known)
        cleanup_errors=[]
        try:
            if 'control' in f:
                control=self.transport.request(f['control'],variables);test.assertIn(control['status'],range(200,300),'Control request must succeed before interpreting a negative result')
            for recipe in f.get('setup',[]):
                response=self.transport.request(recipe,variables);test.assertIn(response['status'],recipe.get('expected_statuses',[200,201,204]))
                for name,path in recipe.get('capture',{}).items():variables[name]=pointer(response,path)
            response=self.transport.request(f['request'],variables)
            observed=pointer(response,f.get('select','/body'))
            if 'project' in f:
                observed={key:pointer(response,path) for key,path in f['project'].items()}
            expected=render(case.get('expected'),variables)
            assert_oracle(test,case,response,observed,expected)
        finally:
            for recipe in reversed(f.get('cleanup',[])):
                try:
                    response=self.transport.request(recipe,variables)
                    if response['status'] not in recipe.get('expected_statuses',[200,204,404]):cleanup_errors.append('Cleanup returned '+str(response['status']))
                except Exception as e:cleanup_errors.append(type(e).__name__+': cleanup failed')
            if cleanup_errors:raise AssertionError('; '.join(cleanup_errors))
