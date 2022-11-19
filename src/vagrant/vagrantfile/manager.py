from pydantic import BaseModel, IPvAnyAddress, PositiveInt
# Solo tengo que agregar y parsear la parte de la lista de las maquinas, el vagranfile no necesita nada

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

    def _write_vagrantfile(self):
        with open('Vagrantfile', 'w') as f:
            f.write('')

    def _set_ip(self):
        pass

    def _set_port(self):
        pass

    def _generate_name(self):
        pass
