// SPDX-License-Identifier: EPL-2.0
// Generated tests derived from GSoSD 5.3.0, PDF pp. 8, 10-13, 18, 21-25, 38.
// This file is injected ONLY into a temporary copy by run_native.py.
package core
import (
 _ "embed"
 "encoding/json"
 "net/http/httptest"
 "regexp"
 "testing"
)
//go:embed gsosd_vectors.json
var gsosdVectors []byte
func sosVectors(t *testing.T) Document { t.Helper();var v Document;if e:=json.Unmarshal(gsosdVectors,&v);e!=nil{t.Fatal(e)};return v }
func TestGSoSDPolicyDecisions(t *testing.T) {
 for _,raw:=range list(sosVectors(t),"policies") { c:=raw.(map[string]any);t.Run(str(c,"id"),func(t *testing.T){
  a:=fixture(t,"consumer-authorization")
  if e:=a.Store.Update(func(d database)error{for _,g:=range list(c,"grants"){v:=g.(map[string]any);if _,_,e:=grantRow(d,obj(v,"request"),str(v,"level"),"TestOperator");e!=nil{return e}};return nil});e!=nil{t.Fatal(e)}
  got,e:=a.granted(httptest.NewRequest("POST","/",nil),obj(c,"query"));if e!=nil||got!=c["expected"]{t.Fatalf("%s: got=%v error=%v expected=%v (PDF p11)",str(c,"id"),got,e,c["expected"])}
 }) }
}
func TestGSoSDMetadataSelection(t *testing.T) {
 for _,raw:=range list(sosVectors(t),"metadata"){c:=raw.(map[string]any);t.Run(str(c,"id"),func(t *testing.T){got,e:=metadataMatch(obj(c,"actual"),obj(c,"requirements"));if e!=nil||got!=c["expected"]{t.Fatalf("metadata result=%v error=%v expected=%v",got,e,c["expected"])}})}
}
func TestGSoSDCanonicalIdentifiers(t *testing.T) {
 for _,raw:=range list(sosVectors(t),"canonical"){c:=raw.(map[string]any);t.Run(str(c,"id"),func(t *testing.T){
  d:=database{};req:=Document{"provider":"TestProvider","cloud":"LOCAL","targetType":"SERVICE_DEF","target":"testSignal","defaultPolicy":Document{"policyType":"ALL"},"scopedPolicies":Document{}}
  field,value:=str(c,"field"),str(c,"value");patterns:=map[string]string{"provider":`^[A-Z][A-Za-z0-9]*$`,"target":`^[a-z][A-Za-z0-9]*$`,"scope":`^[a-z0-9]+(-[a-z0-9]+)*$`}
  if field=="scope"{req["scopedPolicies"]=Document{value:Document{"policyType":"ALL"}}}else{req[field]=value}
  row,_,err:=grantRow(d,req,"MGMT","TestOperator")
  inputCanonical:=regexp.MustCompile(patterns[field]).MatchString(value)
  if err!=nil{if inputCanonical{t.Fatalf("canonical identifier rejected: %v",err)};return}
  actual:=str(row,field);if field=="scope"{for k:=range obj(row,"scopedPolicies"){actual=k}}
  if !regexp.MustCompile(patterns[field]).MatchString(actual){t.Fatalf("stored identifier %q is not canonical (PDF Table1 p8); rejection or canonical normalization required",actual)}
 })}
}
func TestGSoSDAMQPTransport(t *testing.T) {
 for _,tc:=range []struct{name,url string;valid bool;port int}{
  {"secure-default","amqps://broker",true,5671},{"secure-explicit","amqps://broker:5671",true,5671},{"plaintext","amqp://broker:5672",false,0},{"mqtt-not-monitor","mqtts://broker:8883",false,0},{"missing-host","amqps://",false,0},{"embedded-password","amqps://user:password@broker",false,0},
 }{t.Run(tc.name,func(t *testing.T){a:=fixture(t,"authentication");a.Config.AMQPURL=tc.url;_,port,e:=a.amqpEndpoint();if tc.valid {if e!=nil||port!=tc.port{t.Fatalf("%d %v",port,e)}}else if e==nil{t.Fatal("unsafe monitoring transport accepted (PDF p18)")}})}
}
func TestGSoSDCoreServiceMatrix(t *testing.T){
 expected:=map[string][]string{
 "authentication":{"identity","identityManagement","generalManagement"},
 "consumer-authorization":{"authorization","authorizationToken","authorizationManagement","authorizationTokenManagement","generalManagement"},
 "serviceorchestration-dynamic":{"serviceOrchestration","serviceOrchestrationPushManagement","serviceOrchestrationLockManagement","serviceOrchestrationHistoryManagement","generalManagement"},
 "serviceorchestration-simple":{"serviceOrchestration","serviceOrchestrationSimpleStoreManagement","serviceOrchestrationPushManagement","serviceOrchestrationHistoryManagement","generalManagement"},
 }
 for role,defs:=range expected{a:=fixture(t,role);for _,def:=range defs{t.Run(role+"/"+def,func(t *testing.T){for _,s:=range a.Services(){if s.Definition==def{return}};t.Fatal("required PDF p9/p38 service absent",def)})}}
}
