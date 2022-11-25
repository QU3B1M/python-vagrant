from pydantic import IPvAnyAddress
from pydantic.errors import IPvAnyAddressError


def is_valid_ip(ip: str) -> bool:
    """Verify if an IP is valid.

    Parameters
    ----------
        ip (str): IP to validate.
    Return
    ------
        bool: True if ip is valid.
    """
    try:
        IPvAnyAddress.validate(ip)
        return True
    except IPvAnyAddressError:
        return False
