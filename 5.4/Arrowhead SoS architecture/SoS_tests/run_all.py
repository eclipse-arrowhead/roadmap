#!/usr/bin/env python3
"""Run all three layers. Native conformance failures intentionally make exit nonzero."""
from pathlib import Path
import argparse,subprocess,sys
HERE=Path(__file__).resolve().parent
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--profile',type=Path);p.add_argument('--allow-mutations',action='store_true');a=p.parse_args();statuses=[]
 for script in ['run_selftests.py','run_native.py','run_live.py']:
  cmd=[sys.executable,str(HERE/script)]
  if script=='run_live.py':
   if a.profile:cmd+=['--profile',str(a.profile.resolve())]
   if a.allow_mutations:cmd+=['--allow-mutations']
  statuses.append(subprocess.run(cmd,cwd=HERE).returncode)
 subprocess.run([sys.executable,str(HERE/'summarize_results.py')],cwd=HERE,check=True)
 sys.exit(1 if any(statuses) else 0)
