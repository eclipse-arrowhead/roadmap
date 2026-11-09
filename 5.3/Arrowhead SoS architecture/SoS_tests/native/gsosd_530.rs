// SPDX-License-Identifier: EPL-2.0
mod common;
use arrowhead_core_rust::*;
use serde_json::{Value,json};
fn vectors()->Value{serde_json::from_str(include_str!("gsosd_vectors.json")).unwrap()}
async fn policy_case(id:&str){
 let c=vectors()["policies"].as_array().unwrap().iter().find(|c|c["id"]==id).unwrap().clone();
 let f=common::Fixture::new("consumer-authorization");
 f.app.store.update(|db|{for g in c["grants"].as_array().unwrap(){authorization::grant(db,g["request"].clone(),g["level"].as_str().unwrap(),"TestOperator")?;}Ok(())}).unwrap();
 assert_eq!(authorization::granted(&f.app,c["query"].clone()).await.unwrap(),c["expected"].as_bool().unwrap(),"{} PDF p11",id);
}
fn metadata_case(id:&str){let v=vectors();let c=v["metadata"].as_array().unwrap().iter().find(|c|c["id"]==id).unwrap();assert_eq!(metadata_match(&c["actual"],&c["requirements"]).unwrap(),c["expected"].as_bool().unwrap());}
fn canonical_case(id:&str){
 let v=vectors();let c=v["canonical"].as_array().unwrap().iter().find(|c|c["id"]==id).unwrap();let field=c["field"].as_str().unwrap();let value=c["value"].as_str().unwrap();
 let pattern=match field{"provider"=>"^[A-Z][A-Za-z0-9]*$","target"=>"^[a-z][A-Za-z0-9]*$",_=>"^[a-z0-9]+(-[a-z0-9]+)*$"};let re=regex::Regex::new(pattern).unwrap();
 let mut req=json!({"provider":"TestProvider","cloud":"LOCAL","targetType":"SERVICE_DEF","target":"testSignal","defaultPolicy":{"policyType":"ALL"},"scopedPolicies":{}});
 if field=="scope"{req["scopedPolicies"][value]=json!({"policyType":"ALL"});}else{req[field]=value.into();}
 match authorization::grant(&mut Database::new(),req,"MGMT","TestOperator"){
  Err(e)=>assert!(!re.is_match(value),"canonical identifier rejected: {:?}",e),
  Ok(row)=>{if field=="scope"{for key in row["scopedPolicies"].as_object().unwrap().keys(){assert!(re.is_match(key),"noncanonical stored operation {} (PDF p8)",key);}}else{assert!(re.is_match(row[field].as_str().unwrap()),"noncanonical stored identifier {} (PDF p8)",row[field]);}}
 }
}
#[tokio::test]
async fn gsosd_authz_service_def_all_testconsumer(){policy_case("AUTHZ-SERVICE_DEF-all-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_service_def_all_otherconsumer(){policy_case("AUTHZ-SERVICE_DEF-all-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_service_def_whitelist_testconsumer(){policy_case("AUTHZ-SERVICE_DEF-whitelist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_service_def_whitelist_otherconsumer(){policy_case("AUTHZ-SERVICE_DEF-whitelist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_service_def_blacklist_testconsumer(){policy_case("AUTHZ-SERVICE_DEF-blacklist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_service_def_blacklist_otherconsumer(){policy_case("AUTHZ-SERVICE_DEF-blacklist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_service_def_missing_testconsumer(){policy_case("AUTHZ-SERVICE_DEF-missing-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_service_def_missing_otherconsumer(){policy_case("AUTHZ-SERVICE_DEF-missing-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_all_all_testconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-all-all-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_all_all_otherconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-all-all-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_all_whitelist_testconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-all-whitelist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_all_whitelist_otherconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-all-whitelist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_all_blacklist_testconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-all-blacklist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_all_blacklist_otherconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-all-blacklist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_whitelist_all_testconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-whitelist-all-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_whitelist_all_otherconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-whitelist-all-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_whitelist_whitelist_testconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-whitelist-whitelist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_whitelist_whitelist_otherconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-whitelist-whitelist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_whitelist_blacklist_testconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-whitelist-blacklist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_whitelist_blacklist_otherconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-whitelist-blacklist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_blacklist_all_testconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-blacklist-all-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_blacklist_all_otherconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-blacklist-all-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_blacklist_whitelist_testconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-blacklist-whitelist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_blacklist_whitelist_otherconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-blacklist-whitelist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_blacklist_blacklist_testconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-blacklist-blacklist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_service_def_blacklist_blacklist_otherconsumer(){policy_case("AUTHZ-priority-SERVICE_DEF-blacklist-blacklist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_event_type_all_testconsumer(){policy_case("AUTHZ-EVENT_TYPE-all-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_event_type_all_otherconsumer(){policy_case("AUTHZ-EVENT_TYPE-all-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_event_type_whitelist_testconsumer(){policy_case("AUTHZ-EVENT_TYPE-whitelist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_event_type_whitelist_otherconsumer(){policy_case("AUTHZ-EVENT_TYPE-whitelist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_event_type_blacklist_testconsumer(){policy_case("AUTHZ-EVENT_TYPE-blacklist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_event_type_blacklist_otherconsumer(){policy_case("AUTHZ-EVENT_TYPE-blacklist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_event_type_missing_testconsumer(){policy_case("AUTHZ-EVENT_TYPE-missing-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_event_type_missing_otherconsumer(){policy_case("AUTHZ-EVENT_TYPE-missing-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_all_all_testconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-all-all-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_all_all_otherconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-all-all-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_all_whitelist_testconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-all-whitelist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_all_whitelist_otherconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-all-whitelist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_all_blacklist_testconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-all-blacklist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_all_blacklist_otherconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-all-blacklist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_whitelist_all_testconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-whitelist-all-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_whitelist_all_otherconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-whitelist-all-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_whitelist_whitelist_testconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-whitelist-whitelist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_whitelist_whitelist_otherconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-whitelist-whitelist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_whitelist_blacklist_testconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-whitelist-blacklist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_whitelist_blacklist_otherconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-whitelist-blacklist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_blacklist_all_testconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-blacklist-all-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_blacklist_all_otherconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-blacklist-all-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_blacklist_whitelist_testconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-blacklist-whitelist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_blacklist_whitelist_otherconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-blacklist-whitelist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_blacklist_blacklist_testconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-blacklist-blacklist-TestConsumer").await;}
#[tokio::test]
async fn gsosd_authz_priority_event_type_blacklist_blacklist_otherconsumer(){policy_case("AUTHZ-priority-EVENT_TYPE-blacklist-blacklist-OtherConsumer").await;}
#[tokio::test]
async fn gsosd_authz_isolation_provider(){policy_case("AUTHZ-isolation-provider").await;}
#[tokio::test]
async fn gsosd_authz_isolation_consumer(){policy_case("AUTHZ-isolation-consumer").await;}
#[tokio::test]
async fn gsosd_authz_isolation_cloud(){policy_case("AUTHZ-isolation-cloud").await;}
#[tokio::test]
async fn gsosd_authz_isolation_target(){policy_case("AUTHZ-isolation-target").await;}
#[tokio::test]
async fn gsosd_authz_isolation_targettype(){policy_case("AUTHZ-isolation-targetType").await;}
#[tokio::test]
async fn gsosd_authz_operation_all_read(){policy_case("AUTHZ-operation-all-read").await;}
#[tokio::test]
async fn gsosd_authz_operation_all_write(){policy_case("AUTHZ-operation-all-write").await;}
#[tokio::test]
async fn gsosd_authz_operation_whitelist_read(){policy_case("AUTHZ-operation-whitelist-read").await;}
#[tokio::test]
async fn gsosd_authz_operation_whitelist_write(){policy_case("AUTHZ-operation-whitelist-write").await;}
#[tokio::test]
async fn gsosd_authz_operation_blacklist_read(){policy_case("AUTHZ-operation-blacklist-read").await;}
#[tokio::test]
async fn gsosd_authz_operation_blacklist_write(){policy_case("AUTHZ-operation-blacklist-write").await;}
#[test]
fn gsosd_meta_01(){metadata_case("META-01");}
#[test]
fn gsosd_meta_02(){metadata_case("META-02");}
#[test]
fn gsosd_meta_03(){metadata_case("META-03");}
#[test]
fn gsosd_meta_04(){metadata_case("META-04");}
#[test]
fn gsosd_meta_05(){metadata_case("META-05");}
#[test]
fn gsosd_meta_06(){metadata_case("META-06");}
#[test]
fn gsosd_meta_07(){metadata_case("META-07");}
#[test]
fn gsosd_meta_08(){metadata_case("META-08");}
#[test]
fn gsosd_meta_09(){metadata_case("META-09");}
#[test]
fn gsosd_meta_10(){metadata_case("META-10");}
#[test]
fn gsosd_name_provider_01(){canonical_case("NAME-provider-01");}
#[test]
fn gsosd_name_provider_02(){canonical_case("NAME-provider-02");}
#[test]
fn gsosd_name_provider_03(){canonical_case("NAME-provider-03");}
#[test]
fn gsosd_name_provider_04(){canonical_case("NAME-provider-04");}
#[test]
fn gsosd_name_provider_05(){canonical_case("NAME-provider-05");}
#[test]
fn gsosd_name_provider_06(){canonical_case("NAME-provider-06");}
#[test]
fn gsosd_name_target_07(){canonical_case("NAME-target-07");}
#[test]
fn gsosd_name_target_08(){canonical_case("NAME-target-08");}
#[test]
fn gsosd_name_target_09(){canonical_case("NAME-target-09");}
#[test]
fn gsosd_name_target_10(){canonical_case("NAME-target-10");}
#[test]
fn gsosd_name_target_11(){canonical_case("NAME-target-11");}
#[test]
fn gsosd_name_target_12(){canonical_case("NAME-target-12");}
#[test]
fn gsosd_name_scope_13(){canonical_case("NAME-scope-13");}
#[test]
fn gsosd_name_scope_14(){canonical_case("NAME-scope-14");}
#[test]
fn gsosd_name_scope_15(){canonical_case("NAME-scope-15");}
#[test]
fn gsosd_name_scope_16(){canonical_case("NAME-scope-16");}
#[test]
fn gsosd_name_scope_17(){canonical_case("NAME-scope-17");}
#[test]
fn gsosd_name_scope_18(){canonical_case("NAME-scope-18");}
#[test]
fn gsosd_matrix_serviceregistry_servicediscovery(){assert!(contracts::services("serviceregistry").iter().any(|s|s.definition=="serviceDiscovery"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_serviceregistry_systemdiscovery(){assert!(contracts::services("serviceregistry").iter().any(|s|s.definition=="systemDiscovery"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_serviceregistry_devicediscovery(){assert!(contracts::services("serviceregistry").iter().any(|s|s.definition=="deviceDiscovery"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_serviceregistry_serviceregistrymanagement(){assert!(contracts::services("serviceregistry").iter().any(|s|s.definition=="serviceRegistryManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_serviceregistry_generalmanagement(){assert!(contracts::services("serviceregistry").iter().any(|s|s.definition=="generalManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_authentication_identity(){assert!(contracts::services("authentication").iter().any(|s|s.definition=="identity"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_authentication_identitymanagement(){assert!(contracts::services("authentication").iter().any(|s|s.definition=="identityManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_authentication_generalmanagement(){assert!(contracts::services("authentication").iter().any(|s|s.definition=="generalManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_consumerauthorization_authorization(){assert!(contracts::services("consumer-authorization").iter().any(|s|s.definition=="authorization"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_consumerauthorization_authorizationtoken(){assert!(contracts::services("consumer-authorization").iter().any(|s|s.definition=="authorizationToken"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_consumerauthorization_authorizationmanagement(){assert!(contracts::services("consumer-authorization").iter().any(|s|s.definition=="authorizationManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_consumerauthorization_authorizationtokenmanagement(){assert!(contracts::services("consumer-authorization").iter().any(|s|s.definition=="authorizationTokenManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_consumerauthorization_generalmanagement(){assert!(contracts::services("consumer-authorization").iter().any(|s|s.definition=="generalManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_dynamicserviceorchestration_serviceorchestration(){assert!(contracts::services("serviceorchestration-dynamic").iter().any(|s|s.definition=="serviceOrchestration"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_dynamicserviceorchestration_serviceorchestrationpushmanagement(){assert!(contracts::services("serviceorchestration-dynamic").iter().any(|s|s.definition=="serviceOrchestrationPushManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_dynamicserviceorchestration_serviceorchestrationlockmanagement(){assert!(contracts::services("serviceorchestration-dynamic").iter().any(|s|s.definition=="serviceOrchestrationLockManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_dynamicserviceorchestration_serviceorchestrationhistorymanagement(){assert!(contracts::services("serviceorchestration-dynamic").iter().any(|s|s.definition=="serviceOrchestrationHistoryManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_dynamicserviceorchestration_generalmanagement(){assert!(contracts::services("serviceorchestration-dynamic").iter().any(|s|s.definition=="generalManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_simplestoreserviceorchestration_serviceorchestration(){assert!(contracts::services("serviceorchestration-simple").iter().any(|s|s.definition=="serviceOrchestration"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_simplestoreserviceorchestration_serviceorchestrationsimplestoremanagement(){assert!(contracts::services("serviceorchestration-simple").iter().any(|s|s.definition=="serviceOrchestrationSimpleStoreManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_simplestoreserviceorchestration_serviceorchestrationpushmanagement(){assert!(contracts::services("serviceorchestration-simple").iter().any(|s|s.definition=="serviceOrchestrationPushManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_simplestoreserviceorchestration_serviceorchestrationhistorymanagement(){assert!(contracts::services("serviceorchestration-simple").iter().any(|s|s.definition=="serviceOrchestrationHistoryManagement"),"PDF p9/p38 service absent");}
#[test]
fn gsosd_matrix_simplestoreserviceorchestration_generalmanagement(){assert!(contracts::services("serviceorchestration-simple").iter().any(|s|s.definition=="generalManagement"),"PDF p9/p38 service absent");}
