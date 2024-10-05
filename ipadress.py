import re
import ipaddress

class IPAddressHandler:
    def __init__(self, ip_address: str):
        self.ip_address = ip_address

    def is_valid_ip(self) -> bool:
        try:
            ipaddress.ip_address(self.ip_address)
            return True
        except ValueError:
            return False

    def is_broadcast_ip(self, subnet_mask: str) -> bool:
        if not self.is_valid_ip():
            return False
        try:
            network = ipaddress.IPv4Network(f"0.0.0.0/{subnet_mask}", strict=False)
            ip_obj = ipaddress.IPv4Address(self.ip_address)
            return ip_obj == network.broadcast_address
        except ValueError:
            return False

    def get_ip_type(self) -> str:
        if not self.is_valid_ip():
            return 
        
        ip_obj = ipaddress.ip_address(self.ip_address)
        
        if ip_obj.is_private:
            return 
        elif ip_obj.is_global:
            return 
        elif ip_obj.is_multicast:
            return 
        elif ip_obj.is_loopback:
            return 
        elif ip_obj.is_link_local:
            return 
        elif ip_obj.is_reserved:
            return 
        else:
            return 

    def get_broadcast_address(self, subnet_mask: str) -> str:
        if not self.is_valid_ip():
            return 
        try:
            network = ipaddress.IPv4Network(f"{self.ip_address}/{subnet_mask}", strict=False)
            return str(network.broadcast_address)
        except ValueError:
            return 


ip_handler = IPAddressHandler("192.168.1.100")

print("Platná IP:", ip_handler.is_valid_ip())  
print("Typ IP:", ip_handler.get_ip_type())  
print("Broadcast adresa:", ip_handler.get_broadcast_address("255.255.255.0"))  
print("Je broadcast IP:", ip_handler.is_broadcast_ip("255.255.255.0"))  
