import pytest


machines = [
    pytest.param({'name': 'test', 'os': 'ubuntu/trusty64',
                  'ip': '192.168.56.10', 'port': 2020}),
    pytest.param({'name': 'test1', 'os': 'ubuntu/trusty64',
                  'ip': '192.168.56.10', 'shared_folder': '.',
                  'port': 2020}),
    pytest.param({'name': 'test', 'os': 'ubuntu/trusty64',
                  'ip': '192.168.56.10', 'shared_folder': '.',
                  'port': 2020, 'ram': 2048, 'cpu': 2})
]


invalid_machines = [
    pytest.param({'name': 'test', 'os': 'ubuntu/trusty64',
                  'ip': '192.168.5610', 'port': 2020}),
    pytest.param({'name': 'test1', 'os': 'ubuntu/trusty64',
                  'ip': '192.168.56.10', 'shared_folder': 'asdasdasd',
                  'port': 2020})
]
