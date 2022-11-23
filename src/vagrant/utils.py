from pydantic import IPvAnyAddress
from pydantic.errors import IPvAnyAddressError


def is_valid_ip(ip: str) -> bool:
    try:
        IPvAnyAddress.validate(ip)
        return True
    except IPvAnyAddressError:
        return False
