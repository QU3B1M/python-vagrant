from os import path

from pydantic import BaseModel, PositiveInt
from pydantic import validator

from src.vagrant.utils import is_valid_ip


class VagrantMachine(BaseModel):

    name: str
    os: str
    ip: str
    shared_folder: str = '.'
    port: PositiveInt
    ram: PositiveInt = 1024
    cpu: PositiveInt = 1

    @validator('ip')
    def ip_must_be_valid(cls, v):
        """Validates the IP has the correct format."""
        if not is_valid_ip(v):
            raise ValueError('IP is not valid.')
        return v

    @validator('shared_folder')
    def path_must_be_valid(cls, v):
        """Validates the Path exists."""
        if not path.exists(v):
            raise ValueError('Path does not exists.')
        return v
