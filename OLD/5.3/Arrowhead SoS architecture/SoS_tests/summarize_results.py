#!/usr/bin/env python3
"""Update current result summary and JUnit XML from actual recorded outcomes."""
from pathlib import Path
import json,xml.etree.ElementTree as ET
HERE=Path(__file__).resolve().parent

def main():
 report=HERE/'reports';suites=ET.Element('testsuites');lines=['# Latest recorded outcomes','','These are execution outcomes, not release certification. See RESULTS.md for the original dated run and COVERAGE.md for scope.','','| Group | Pass | Fail/error | Skip |','|---|---:|---:|---:|']
 groups=[]
 p=report/'native-results.json'
 if p.exists():
  for lang,data in json.loads(p.read_text()).get('languages',{}).items():groups.append(('native-'+lang,data.get('cases',[])))
 for label,path in [('deployment','live-results.json'),('harness-self-tests','harness-results.json')]:
  p=report/path
  if p.exists():groups.append((label,json.loads(p.read_text()).get('cases',[])))
 for name,cases in groups:
  passed=sum(c['outcome']=='pass' for c in cases);failed=sum(c['outcome'] in ['fail','error'] for c in cases);skipped=sum(c['outcome']=='skip' for c in cases)
  lines.append(f'| {name} | {passed} | {failed} | {skipped} |')
  suite=ET.SubElement(suites,'testsuite',name=name,tests=str(len(cases)),failures=str(failed),skipped=str(skipped))
  for c in cases:
   test=ET.SubElement(suite,'testcase',classname=name,name=c['id'])
   if c['outcome']=='skip':ET.SubElement(test,'skipped',message=c.get('reason','unconfigured'))
   elif c['outcome'] in ['fail','error']:ET.SubElement(test,'failure',message=c.get('reason','See native raw log'))
 report.mkdir(exist_ok=True);ET.indent(suites);ET.ElementTree(suites).write(report/'junit.xml',encoding='utf-8',xml_declaration=True)
 (HERE/'CURRENT_RESULTS.md').write_text('\n'.join(lines)+'\n')
if __name__=='__main__':main()
