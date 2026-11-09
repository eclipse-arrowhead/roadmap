"""Live tests: absent profiles/fixtures are SKIPPED, never reported as conformance."""
from pathlib import Path
import json,os,re,unittest
from .harness import Executor,HTTPS,MissingFixture
HERE=Path(__file__).resolve().parents[1]
CATALOG=json.loads((HERE/'catalog.json').read_text());SCENARIOS=json.loads((HERE/'scenarios.json').read_text())

def profile():
    path=os.environ.get('SOS_TEST_PROFILE')
    if not path:raise MissingFixture('Set SOS_TEST_PROFILE to an isolated test deployment profile')
    p=Path(path);config=json.loads(p.read_text())
    if not config.get('test_environment'):raise ValueError('Profile requires test_environment=true')
    return config,p.parent

class BehaviorTests(unittest.TestCase):pass
for scenario in SCENARIOS:
    def test(self,c=scenario):
        conf,base=profile();Executor(conf,base,os.environ.get('SOS_ALLOW_MUTATIONS')=='1').execute(self,c)
    test.__doc__=scenario['title']+' [PDF '+','.join(map(str,scenario['pages']))+']'
    setattr(BehaviorTests,'test_'+scenario['id'].replace('-','_'),test)

class RegistrationTests(unittest.TestCase):pass

def registrations(test,system,service):
    conf,base=profile()
    if system not in conf.get('systems',[]):raise MissingFixture('Optional/unconfigured system '+system)
    response=HTTPS(conf,base).request({'endpoint':'registry','method':'POST','path':'/serviceregistry/service-discovery/lookup','actor':'inspector','body':{'providerNames':[system],'serviceDefinitionNames':[service]}},conf.get('variables',{}))
    test.assertEqual(response['status'],200,'Inspector needs direct-discovery permission')
    body=response['body'];test.assertIsInstance(body,dict);rows=body.get('entries');test.assertIsInstance(rows,list);test.assertTrue(rows,'Required registered service absent')
    for row in rows:
        test.assertEqual(row['provider']['name'],system);test.assertEqual(row['serviceDefinition']['name'],service)
    return rows

def protected(test,rows,service):
    secure={'https','mqtts','amqps','ssl'}
    for row in rows:
        test.assertTrue(row.get('interfaces'))
        for interface in row['interfaces']:
            test.assertIn(interface.get('protocol','').lower(),secure,'Default architecture does not advertise plaintext interfaces')
            test.assertNotIn(interface.get('policy'),[None,'NONE','SELF_DECLARED'],'Secure transport alone is not an authenticated service policy')
        if service=='sysMonitor':test.assertTrue(any(i.get('protocol','').lower()=='amqps' for i in row['interfaces']),'sysMonitor must provide AMQPS, not an HTTP echo substitute')

def naming(test,rows):
    for row in rows:
        test.assertRegex(row['provider']['name'],r'^[A-Z][A-Za-z0-9]*$');test.assertRegex(row['serviceDefinition']['name'],r'^[a-z][A-Za-z0-9]*$')
        for i in row['interfaces']:
            test.assertRegex(i['templateName'],r'^[a-z0-9]+(_[a-z0-9]+)*$')
            ops=i.get('properties',{}).get('operations',{})
            test.assertIsInstance(ops,(dict,list));test.assertTrue(ops,'Registered interface needs named operations')
            for op in ops:test.assertRegex(op,r'^[a-z0-9]+(-[a-z0-9]+)*$')

for system in CATALOG['systems']:
    for service in system['services']:
        for check in ['presence','protected','naming']:
            def test(self,name=system['name'],svc=service,check=check):
                rows=registrations(self,name,svc)
                if check=='protected':protected(self,rows,svc)
                elif check=='naming':naming(self,rows)
            test.__doc__=system['name']+'.'+service+' '+check+' [PDF pp.5,8-10,15,18,38-39]'
            setattr(RegistrationTests,'test_'+system['name']+'_'+service+'_'+check,test)
