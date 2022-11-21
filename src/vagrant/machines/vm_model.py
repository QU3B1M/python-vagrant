from pydantic import BaseModel, IPvAnyAddress, PositiveInt, DirectoryPath


class VagrantMachine(BaseModel):

    name: str
    os: str
    ip: str
    port: PositiveInt
    shared_folder: str = '.'
    ram: PositiveInt = 1024
    cpu: PositiveInt = 1
