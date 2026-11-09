#!/usr/bin/env python3
from pathlib import Path
import json,sys,unittest
from run_live import Results
HERE=Path(__file__).resolve().parent
if __name__=='__main__':
 suite=unittest.defaultTestLoader.loadTestsFromName('sos_tests.test_harness')
 result=unittest.TextTestRunner(verbosity=1,resultclass=Results).run(suite)
 (HERE/'reports').mkdir(exist_ok=True)
 (HERE/'reports/harness-results.json').write_text(json.dumps({'kind':'test-harness-self-tests','cases':result.cases,'note':'Runner correctness only; these are not Arrowhead conformance passes.'},indent=2)+'\n')
 sys.exit(0 if result.wasSuccessful() else 1)
