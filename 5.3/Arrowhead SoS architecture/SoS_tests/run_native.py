#!/usr/bin/env python3
"""Execute real Java/Go/Rust source tests in disposable copies; never edit implementations."""
from pathlib import Path
import argparse,hashlib,json,os,re,shutil,subprocess,sys,tempfile,time,tomllib,xml.etree.ElementTree as ET
HERE=Path(__file__).resolve().parent

def root_default():
 for p in [HERE,*HERE.parents]:
  if (p/'Eclipse-Arrowhead-java').is_dir():return p
 return Path('/Users/jerkerdelsing/Work/lule/EISLAB/Project/Eclipse')
def run(cmd,cwd,env,timeout=600):
 try:
  p=subprocess.run([str(x) for x in cmd],cwd=cwd,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout)
  return p.returncode,p.stdout
 except subprocess.TimeoutExpired as e:return 124,(e.stdout or b'').decode() if isinstance(e.stdout,bytes) else (e.stdout or '')
def copy(src,dest):
 def writable_copy(s,d):
  if Path(d).exists():Path(d).chmod(Path(d).stat().st_mode|0o200)
  return shutil.copy2(s,d)
 shutil.copytree(src,dest,ignore=shutil.ignore_patterns('target','.git','node_modules','__pycache__','*.log'),dirs_exist_ok=True,copy_function=writable_copy)
def tool(name,extra=()):
 return shutil.which(name) or next((str(p) for p in extra if Path(p).is_file()),None)
def go(root,tmp,env):
 binary=tool('go',['/usr/local/go/bin/go']);src=root/'Eclipse-Arrowhead-go/ah5-core-go/consumer-authorization'
 if not binary or not src.exists():return {'state':'unavailable','reason':'Go toolchain or primary module missing','cases':[]},''
 dest=tmp/'go';copy(src,dest);pkg=dest/'internal/core'
 shutil.copyfile(HERE/'native/gsosd_530_test.go',pkg/'gsosd_530_test.go');shutil.copyfile(HERE/'native/vectors.json',pkg/'gsosd_vectors.json')
 env={**env,'GOWORK':'off','GOPROXY':'off','GOTOOLCHAIN':'local','GOCACHE':str(tmp/'go-cache')}
 code,out=run([binary,'test','-json','-count=1','./internal/core','-run','^TestGSoSD'],dest,env)
 cases=[]
 for line in out.splitlines():
  try:e=json.loads(line)
  except ValueError:continue
  if e.get('Test') and '/' in e['Test'] and e.get('Action') in ['pass','fail','skip']:cases.append({'id':e['Test'],'outcome':e['Action']})
 return {'state':'executed' if cases else 'build-error','returncode':code,'cases':cases,'source':str(src)},out

def rust(root,tmp,env):
 binary=tool('cargo',['/opt/homebrew/bin/cargo']);src=root/'Eclipse-Arrowhead-rust'
 if not binary or not (src/'ah5-core-rust').exists():return {'state':'unavailable','reason':'Rust toolchain or source missing','cases':[]},''
 dest=tmp/'rust'
 for folder in ['ah5-core-rust','ah5-messaging-rust']:copy(src/folder,dest/folder)
 (dest/'Cargo.toml').write_text('[workspace]\nresolver="3"\nmembers=["ah5-core-rust","ah5-messaging-rust"]\n')
 shutil.copyfile(src/'Cargo.lock',dest/'Cargo.lock');tests=dest/'ah5-core-rust/tests'
 shutil.copyfile(HERE/'native/gsosd_530.rs',tests/'gsosd_530.rs');shutil.copyfile(HERE/'native/vectors.json',tests/'gsosd_vectors.json')
 env={**env,'CARGO_TARGET_DIR':str(tmp/'rust-target')}
 old_packages={(p['name'],p['version'],p.get('source','')) for p in tomllib.loads((src/'Cargo.lock').read_text()).get('package',[])}
 code,out=run([binary,'test','--offline','-p','arrowhead-core-rust','--test','gsosd_530','--','--test-threads=1'],dest,env)
 new_packages={(p['name'],p['version'],p.get('source','')) for p in tomllib.loads((dest/'Cargo.lock').read_text()).get('package',[])}
 if new_packages-old_packages:return {'state':'dependency-drift','returncode':1,'cases':[]},out+'\nDependency set changed from original lockfile'
 cases=[{'id':m[0],'outcome':{'ok':'pass','FAILED':'fail','ignored':'skip'}[m[1]]} for m in re.findall(r'^test (\S+) \.\.\. (ok|FAILED|ignored)',out,re.M)]
 return {'state':'executed' if cases else 'build-error','returncode':code,'cases':cases,'source':str(src)},out

def java(root,tmp,env):
 src=root/'Eclipse-Arrowhead-java/ah5-core-java-spring/consumer-authorization'
 javac=tool('javac',['/Library/Java/JavaVirtualMachines/jdk-22.jdk/Contents/Home/bin/javac']);java_bin=tool('java',['/Library/Java/JavaVirtualMachines/jdk-22.jdk/Contents/Home/bin/java'])
 # On macOS /usr/bin/java may select JDK17. Prefer known current JDK when installed.
 jdk=Path('/Library/Java/JavaVirtualMachines/jdk-22.jdk/Contents/Home/bin')
 if (jdk/'javac').is_file():javac=str(jdk/'javac');java_bin=str(jdk/'java')
 if not javac:return {'state':'unavailable','reason':'JDK missing','cases':[]},''
 reports=list((src/'target/surefire-reports').glob('TEST-*AuthorizationPolicyEngineTest.xml'))
 if not reports:return {'state':'unavailable','reason':'Exact dependency classpath unavailable; build Java source with Maven first','cases':[]},''
 tree=ET.parse(reports[0]);cp=next((x.attrib['value'] for x in tree.findall('./properties/property') if x.attrib['name']=='java.class.path'),'')
 jars=[]
 for item in cp.split(os.pathsep):
  if '/repository/' in item:jars.append(Path.home()/'.m2/repository'/item.split('/repository/',1)[1])
 missing=[str(p) for p in jars if not p.exists()]
 if missing:return {'state':'unavailable','reason':'Missing exact Java dependencies','missing':missing,'cases':[]},''
 dest=tmp/'java';dest.mkdir(exist_ok=True);classes=dest/'classes';classes.mkdir(exist_ok=True)
 # Compile every consumer-authorization production source freshly. Cached class files
 # are not the system under test. Tests use the exact recorded dependency versions.
 sources=list((src/'src/main/java').rglob('*.java'))
 classpath=os.pathsep.join(map(str,jars));test=HERE/'native/SoSAuthorizationEngineTests.java'
 code,out=run([javac,'-encoding','UTF-8','-cp',classpath,'-d',classes,*sources,test],dest,env)
 if code:return {'state':'build-error','returncode':code,'cases':[]},out
 log=dest/'log4j2.xml';log.write_text('<Configuration status="OFF"><Loggers><Root level="off"/></Loggers></Configuration>')
 code,text=run([java_bin,'-Dlog4j2.configurationFile='+str(log),'-cp',str(classes)+os.pathsep+classpath,'SoSAuthorizationEngineTests'],dest,env)
 cases=[{'id':m[1],'outcome':m[0].lower()} for m in re.findall(r'^GSOSD (PASS|FAIL) (\S+)',text,re.M)]
 return {'state':'executed' if cases else 'runtime-error','returncode':code,'cases':cases,'source':str(src),'freshlyCompiledSources':len(sources)},out+text

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=root_default());p.add_argument('--language',choices=['all','java','go','rust'],default='all');p.add_argument('--report-dir',type=Path,default=HERE/'reports');p.add_argument('--work-dir',type=Path);a=p.parse_args()
 a.report_dir.mkdir(parents=True,exist_ok=True);work=a.work_dir or Path(tempfile.mkdtemp(prefix='arrowhead-gsosd530-'));work.mkdir(parents=True,exist_ok=True)
 result={'kind':'native-implementation-tests','sourcePdf':json.loads((HERE/'catalog.json').read_text())['source'],'workDirectory':str(work),'languages':{},'note':'Local component tests do not establish deployed or cross-language wire conformance.'}
 source_hashes={}
 for folder in ['Eclipse-Arrowhead-java/ah5-core-java-spring/consumer-authorization','Eclipse-Arrowhead-go/ah5-core-go/consumer-authorization','Eclipse-Arrowhead-rust/ah5-core-rust','Eclipse-Arrowhead-rust/ah5-messaging-rust']:
  for f in (a.root/folder).rglob('*'):
   if f.is_file() and f.suffix in ['.java','.go','.rs','.toml','.mod','.sum','.lock'] and not any(x in ['target','.git'] for x in f.relative_to(a.root).parts):source_hashes[str(f.relative_to(a.root))]=hashlib.sha256(f.read_bytes()).hexdigest()
 (a.report_dir/'source-fingerprints.json').write_text(json.dumps(source_hashes,indent=2)+'\n')
 for name in (['java','go','rust'] if a.language=='all' else [a.language]):
  start=time.monotonic();r,log=globals()[name](a.root,work,os.environ.copy());r['elapsedSeconds']=round(time.monotonic()-start,2);result['languages'][name]=r;(a.report_dir/(name+'-native.log')).write_text(log);(a.report_dir/(name+'-native-results.json')).write_text(json.dumps(r,indent=2)+'\n')
  counts={key:sum(c['outcome']==key for c in r['cases']) for key in ['pass','fail','skip']};print(name,r['state'],counts,flush=True)
 (a.report_dir/'native-results.json').write_text(json.dumps(result,indent=2)+'\n')
 return 1 if any(r.get('returncode',0)!=0 or r['state']!='executed' for r in result['languages'].values()) else 0
if __name__=='__main__':sys.exit(main())
