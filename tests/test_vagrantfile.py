import pytest

from src.vagrant.vagrantfile import VMsDefiner, VagrantMachine


@pytest.fixture
def restore_definition_file():
    original_data = VMsDefiner.get_defined_machines()
    yield
    VMsDefiner._save_machines(original_data)


def test_add_new_machine(restore_definition_file):
    new_vm = {'name': 'test', 'os': 'ubuntu/trusty64',
              'ip': '192.168.56.10', 'port': 2020}
    new_vm = VagrantMachine(**new_vm)
    VMsDefiner.add_machine(new_vm)
    machines_list = VMsDefiner.get_defined_machines()
    assert [vm for vm in machines_list if vm.name == new_vm.name] is not None
