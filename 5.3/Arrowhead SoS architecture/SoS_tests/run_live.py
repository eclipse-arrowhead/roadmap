#!/usr/bin/env python3
"""Run configured HTTPS deployment scenarios; missing fixtures are explicit skips."""
from pathlib import Path
import argparse,datetime,json,os,sys,unittest
HERE=Path(__file__).resolve().parent
class Results(unittest.TextTestResult):
    def __init__(self,*args,**kwargs):super().__init__(*args,**kwargs);self.cases=[]
    def addSuccess(self,t):super().addSuccess(t);self.cases.append({'id':t.id(),'outcome':'pass'})
    def addSkip(self,t,reason):super().addSkip(t,reason);self.cases.append({'id':t.id(),'outcome':'skip','reason':reason})
    def addFailure(self,t,err):super().addFailure(t,err);self.cases.append({'id':t.id(),'outcome':'fail','reason':str(err[1])})
    def addError(self,t,err):super().addError(t,err);self.cases.append({'id':t.id(),'outcome':'error','reason':str(err[1])})
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--profile',type=Path);p.add_argument('--allow-mutations',action='store_true');p.add_argument('--filter',default='');p.add_argument('--report',type=Path,default=HERE/'reports/live-results.json');a=p.parse_args()
    if a.profile:os.environ['SOS_TEST_PROFILE']=str(a.profile.resolve())
    if a.allow_mutations:os.environ['SOS_ALLOW_MUTATIONS']='1'
    else:os.environ.pop('SOS_ALLOW_MUTATIONS',None)
    suite=unittest.defaultTestLoader.loadTestsFromName('sos_tests.test_live')
    def flatten(s):
        for x in s:
            if isinstance(x,unittest.TestSuite):yield from flatten(x)
            elif not a.filter or a.filter in x.id():yield x
    result=unittest.TextTestRunner(verbosity=1,resultclass=Results).run(unittest.TestSuite(flatten(suite)))
    doc={'kind':'live-deployment-tests','cases':result.cases,'testsRun':result.testsRun,'passed':sum(c['outcome']=='pass' for c in result.cases),'skipped':len(result.skipped),'failures':len(result.failures),'errors':len(result.errors),'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'note':'Skipped cases have not tested an implementation. No profile means no network requests.'}
    a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_text(json.dumps(doc,indent=2)+'\n');return 0 if result.wasSuccessful() else 1
if __name__=='__main__':sys.exit(main())
