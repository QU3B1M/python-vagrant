import json
import os
from pathlib import Path

from .vm_model import VagrantMachine


class VMsDefiner:

    config_file = f'{Path(__file__).parents[1]}/vagrantfile/vms.config.json'

    @classmethod
    def add_machine(cls, new_vm: VagrantMachine) -> None:
        if not isinstance(new_vm, VagrantMachine):
            new_vm = VagrantMachine(**new_vm)
        vms_list = cls.get_defined_machines()

        if cls._value_is_in_use(vms_list, 'name', new_vm.name):
            raise ValueError(f'VM name {new_vm.name} already in use.')
        if cls._value_is_in_use(vms_list, 'ip', new_vm.ip):
            raise ValueError(f'VM IP {new_vm.ip} already in use.')
        if cls._value_is_in_use(vms_list, 'port', new_vm.port):
            raise ValueError(f'VM binded port {new_vm.port} already in use.')

        vms_list.append(new_vm)
        cls._save_machines(vms_list)

    @classmethod
    def get_defined_machines(cls) -> list[VagrantMachine]:
        if os.stat(cls.config_file).st_size == 0:
            return []
        with open(cls.config_file) as f:
            machines = json.load(f)
        return [VagrantMachine(**machine) for machine in machines]

    @classmethod
    def delete_machine(cls, name: str) -> None:
        vms_list = cls.get_defined_machines()
        vms_list = [vm for vm in vms_list if vm.name != name]
        cls._save_machines(vms_list)

    @classmethod
    def _save_machines(cls, machines: list[VagrantMachine]) -> None:
        dict_machines = [machine.dict() for machine in machines]
        with open(cls.config_file, 'w') as f:
            f.write(json.dumps(dict_machines))

    @classmethod
    def _value_is_in_use(cls, list, key, value):
        return bool([i for i in list if getattr(i, key) == value])
