// SPDX-License-Identifier: EPL-2.0
// GSoSD 5.3.0 pp.11,21,23-24. Tests the real Java policy engine;
// the database lookup boundary supplies already-relevant rows, with no database/network.
import java.lang.reflect.Field;
import java.util.*;
import eu.arrowhead.authorization.service.engine.AuthorizationPolicyEngine;
import eu.arrowhead.authorization.service.dto.DTOConverter;
import eu.arrowhead.authorization.service.dto.NormalizedVerifyRequest;
import eu.arrowhead.authorization.jpa.service.AuthorizationPolicyDbService;
import eu.arrowhead.authorization.jpa.entity.*;
import eu.arrowhead.dto.enums.*;
import org.springframework.data.util.Pair;

public class SoSAuthorizationEngineTests {
  static class Rows extends AuthorizationPolicyDbService {
    final String providerKind, managementKind;
    int providerLookups;
    Rows(String providerKind,String managementKind){this.providerKind=providerKind;this.managementKind=managementKind;}
    @Override public Optional<Pair<? extends AuthPolicyHeader,List<AuthPolicy>>> findRelevantPolicies(AuthorizationLevel level,NormalizedVerifyRequest request){
      if(level==AuthorizationLevel.PROVIDER)providerLookups++;
      String kind=level==AuthorizationLevel.MGMT?managementKind:providerKind;
      if(kind.equals("NONE"))return Optional.empty();
      AuthPolicyHeader header=new AuthMgmtPolicyHeader("test",request.targetType(),request.cloud(),request.provider(),request.target(),null,"TestOperator");
      AuthPolicy policy=new AuthPolicy(level,1,"*",AuthorizationPolicyType.valueOf(kind),kind.equals("ALL")?null:"TestConsumer");
      return Optional.of(Pair.of(header,List.of(policy)));
    }
  }
  static boolean allows(String kind,String consumer){return kind.equals("ALL")||kind.equals("WHITELIST")&&consumer.equals("TestConsumer")||kind.equals("BLACKLIST")&&!consumer.equals("TestConsumer");}
  static void inject(Object obj,String name,Object value)throws Exception{Field f=obj.getClass().getDeclaredField(name);f.setAccessible(true);f.set(obj,value);}
  public static void main(String[] args)throws Exception{
    int failures=0;
    for(AuthorizationTargetType target:AuthorizationTargetType.values())for(String consumer:List.of("TestConsumer","OtherConsumer"))for(String provider:List.of("NONE","ALL","WHITELIST","BLACKLIST"))for(String management:List.of("NONE","ALL","WHITELIST","BLACKLIST")){
      String id="JAVA-AUTHZ-"+target+"-"+consumer+"-"+provider+"-"+management;
      try{
        Rows rows=new Rows(provider,management);AuthorizationPolicyEngine engine=new AuthorizationPolicyEngine();inject(engine,"dbService",rows);inject(engine,"dtoConverter",new DTOConverter());
        boolean actual=engine.isAccessGranted(new NormalizedVerifyRequest("TestProvider",consumer,"LOCAL",target,"testSignal","read"));
        boolean expected=allows(management.equals("NONE")?provider:management,consumer);
        if(actual!=expected)throw new AssertionError("expected="+expected+", actual="+actual);
        if(!management.equals("NONE")&&rows.providerLookups!=0)throw new AssertionError("management decision did not short circuit provider lookup");
        System.out.println("GSOSD PASS "+id);
      }catch(Throwable e){failures++;System.out.println("GSOSD FAIL "+id+" "+e.getClass().getSimpleName()+": "+e.getMessage());}
    }
    if(failures>0)System.exit(1);
  }
}
