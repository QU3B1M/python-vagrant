import pytest

from pydantic import ValidationError

from src.vagrant.machines import VMsDefiner, VagrantMachine
from .cases.vms_definition import machines, invalid_machines


@pytest.mark.parametrize("machine", machines)
def test_add_new_machine_valid(machine, restore_definition_file):
    machine = VagrantMachine(**machine)
    VMsDefiner.add_machine(machine)
    machines_list = VMsDefiner.get_defined_machines()
    assert [vm for vm in machines_list if vm.name == machine.name]


@pytest.mark.parametrize("machine", invalid_machines)
def test_add_new_machine_invalid(machine, restore_definition_file):
    with pytest.raises(ValidationError):
        machine = VagrantMachine(**machine)
        VMsDefiner.add_machine(machine)
    machines_list = VMsDefiner.get_defined_machines()
    assert not [vm for vm in machines_list if vm.name == machine['name']]
