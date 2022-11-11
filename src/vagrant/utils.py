import ipaddress

def is_valid_ipv4(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except TypeError:
        return False
