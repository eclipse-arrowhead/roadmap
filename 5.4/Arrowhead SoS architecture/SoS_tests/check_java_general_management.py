"""Check six real Java management endpoints using an isolated Sysop/consumer profile.

Run with --profile PATH --report PATH. The profile needs trusted cloud CA,
inspector (Sysop) and consumer client certificates and token environment names.
Individual endpoint origins can override the local Java cloud port defaults.
This verifier performs read-only requests and never creates identities or policies.
"""
import argparse
import copy
import json
from pathlib import Path
from sos_tests.harness import HTTPS, ConfigurationError

SYSTEMS = [('AIGym', 'aigym', 8478), ('CertificateAuthority', 'certificate-authority', 8448),
           ('DataManager', 'datamanager', 8461), ('GateTunnel', 'gatetunnel', 8453),
           ('Gatekeeper', 'gatekeeper', 8449), ('SysMonitor', 'sysmonitor', 8475)]

def check(profile, base_dir):
    if not profile.get('test_environment'):
        raise ConfigurationError('An explicit test_environment is required')
    p = copy.deepcopy(profile)
    p['actors']['withoutToken'] = {k: v for k, v in p['actors']['consumer'].items() if k != 'token_env'}
    checks = []
    for system, role, port in SYSTEMS:
        p['endpoints'].setdefault(role, 'https://127.0.0.1:' + str(port))
        for actor, expected in [('inspector', 200), ('consumer', 403), ('withoutToken', 401)]:
            response = HTTPS(p, base_dir).request({'endpoint': role, 'actor': actor,
                'path': '/' + role + '/mgmt/general/status', 'method': 'GET'}, {})
            checks.append({'system': system, 'actor': actor, 'expectedStatus': expected,
                           'actualStatus': response['status'], 'passed': response['status'] == expected})
    return checks

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    results = check(json.loads(args.profile.read_text()), args.profile.parent)
    args.report.write_text(json.dumps(results, indent=2) + '\n')
    print(f"{sum(item['passed'] for item in results)}/{len(results)} checks passed")
    raise SystemExit(0 if all(item['passed'] for item in results) else 1)
