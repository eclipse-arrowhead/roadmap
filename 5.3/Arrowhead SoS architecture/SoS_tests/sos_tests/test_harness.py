"""Runner self-tests only: these do not assert Arrowhead implementation conformance."""
import unittest
from .harness import *

class Fake:
    def __init__(self,responses):self.responses=iter(responses);self.calls=[]
    def request(self,recipe,variables):self.calls.append(render(recipe,variables));return next(self.responses)

class HarnessTests(unittest.TestCase):
    def test_json_pointer_arrays_and_escaping(self):self.assertEqual(pointer({'a/b':[{'~key':3}]},'/a~1b/0/~0key'),3)
    def test_missing_pointer_fails(self):
        with self.assertRaises(AssertionError):pointer({},'/missing')
    def test_root_pointer(self):self.assertEqual(pointer([1],''),[1])
    def test_typed_interpolation(self):self.assertIs(render('${flag}',{'flag':False}),False)
    def test_nested_url_variable(self):self.assertEqual(render('/${url:id}',{'id':'PR|${provider}','provider':'SystemA'}),'/PR%7CSystemA')
    def test_variable_cycles_are_errors(self):
        with self.assertRaises(ConfigurationError):render('${x}',{'x':'${y}','y':'${x}'})
    def test_missing_variable_skips(self):
        with self.assertRaises(MissingFixture):render('${missing}',{})
    def test_nested_interpolation(self):self.assertEqual(render({'a':['prefix-${name}']},{'name':'x'}),{'a':['prefix-x']})
    def test_plaintext_endpoint_refused(self):
        client=HTTPS({'endpoints':{'r':'http://localhost'}},'.')
        with self.assertRaises(ConfigurationError):client.request({'endpoint':'r','path':'/'},{})
    def test_redirects_refused(self):
        with self.assertRaises(ConfigurationError):NoRedirect().redirect_request(None,None,None,None,None,None)
    def test_error_is_not_tls_rejection(self):
        with self.assertRaises(AssertionError):assert_oracle(self,{'predicate':'tls_rejected','title':'TLS'},{'status':503,'tls_rejected':False},None)
    def test_authentication_failure_is_not_success(self):
        with self.assertRaises(AssertionError):assert_oracle(self,{'predicate':'equals'},{'status':401},False,False)
    def test_not_found_is_not_authorization_denial(self):
        with self.assertRaises(AssertionError):assert_oracle(self,{'predicate':'denied'},{'status':404},None)
    def test_boolean_is_not_zero(self):
        with self.assertRaises(AssertionError):assert_oracle(self,{'predicate':'equals'},{'status':200},0,False)
    def test_wrong_equality_fails(self):
        with self.assertRaises(AssertionError):assert_oracle(self,{'predicate':'equals'},{'status':200},'wrong','right')
    def test_empty_only_accepts_collections(self):
        with self.assertRaises(AssertionError):assert_oracle(self,{'predicate':'empty'},{'status':200},None)
    def test_subset_detects_unauthorized_provider(self):
        with self.assertRaises(AssertionError):assert_oracle(self,{'predicate':'subset'},{'status':200},['Allowed','Forbidden'],['Allowed'])
    def test_snapshot_detects_partial_update(self):
        with self.assertRaises(AssertionError):assert_oracle(self,{'predicate':'one_of'},{'status':200},['old','new'],[['old'],['new']])
    def test_telemetry_rejects_missing_sequence(self):
        with self.assertRaises(AssertionError):assert_oracle(self,{'predicate':'telemetry'},{'status':200},{'provider':'X'},'X')
    def test_telemetry_valid(self):
        value={'provider':'SystemA','observationType':'echo','sourceTime':'2026-11-03T12:00:00Z','sequence':1,'value':{'status':'alive'},'unit':None,'quality':'good'}
        assert_oracle(self,{'predicate':'telemetry'},{'status':200},value,'SystemA')
    def fixture(self,entry):return {'test_environment':True,'isolated':True,'scenarios':{'X':entry}}
    def test_missing_live_fixture_skips(self):
        with self.assertRaises(MissingFixture):Executor({},'.',transport=Fake([])).execute(self,{'id':'X'})
    def test_mutation_gate(self):
        entry={'request':{'method':'PUT','path':'/object'}};fake=Fake([])
        with self.assertRaises(MissingFixture):Executor(self.fixture(entry),'.',transport=fake).execute(self,{'id':'X','predicate':'nonempty'})
        self.assertFalse(fake.calls)
    def test_preflight_before_mutation(self):
        entry={'setup':[{'method':'PUT','path':'/object'}],'request':{'method':'GET','path':'/${missing}'}};fake=Fake([])
        with self.assertRaises(MissingFixture):Executor(self.fixture(entry),'.',True,fake).execute(self,{'id':'X','predicate':'nonempty'})
        self.assertFalse(fake.calls)
    def test_negative_case_needs_control(self):
        entry={'request':{'method':'GET','path':'/protected'}}
        with self.assertRaises(MissingFixture):Executor(self.fixture(entry),'.',transport=Fake([])).execute(self,{'id':'X','predicate':'denied'})
    def test_cleanup_runs_after_failed_assertion(self):
        entry={'request':{'method':'GET','path':'/object'},'cleanup':[{'method':'DELETE','path':'/object'}]};fake=Fake([{'status':200,'body':False},{'status':204}])
        with self.assertRaises(AssertionError):Executor(self.fixture(entry),'.',True,fake).execute(self,{'id':'X','predicate':'equals','expected':True})
        self.assertEqual(len(fake.calls),2);self.assertEqual(fake.calls[-1]['method'],'DELETE')
    def test_setup_capture_and_cleanup(self):
        entry={'setup':[{'method':'PUT','path':'/object','capture':{'id':'/body/id'}}],'request':{'method':'GET','path':'/object/${id}'},'select':'/body','cleanup':[{'method':'DELETE','path':'/object/${id}'}]}
        fake=Fake([{'status':201,'body':{'id':'123'}},{'status':200,'body':'present'},{'status':204}]);Executor(self.fixture(entry),'.',True,fake).execute(self,{'id':'X','predicate':'equals','expected':'present'})
        self.assertEqual(fake.calls[-1]['path'],'/object/123')
    def test_unknown_oracle_is_error(self):
        with self.assertRaises(ConfigurationError):assert_oracle(self,{'predicate':'typo'},{'status':200},True)
