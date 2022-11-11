from pydantic import BaseModel, IPvAnyAddress, PositiveInt

from utils import is_valid_ipv4


class VagrantMachine(BaseModel):

    ip: IPvAnyAddress
    name: str
    os: str
    ram: PositiveInt = 1024
    cpu: PositiveInt = 1
    port: PositiveInt


class VagrantFile:
    def __init__(self) -> None:
        pass

    def add_machine(self, name: str, os: str, ram: int, cpu: int, ip: str, port: int):
        pass

    def write_vagrantfile(self):
        pass

    def _set_ip(self):
        pass

    def _set_port(self):
        pass

    def _generate_name(self):
        pass
