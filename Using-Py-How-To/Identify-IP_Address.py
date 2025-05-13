import ipaddress

def check_ip(input_data):
    try:
        ip_obj = ipaddress.ip_address(input_data)
        if isinstance(ip_obj, ipaddress.IPv4Address):
            return "Valid IPv4 Address"
        elif isinstance(ip_obj, ipaddress.IPv6Address):
            return "Valid IPv6 Address"
    except ValueError:
        return "Not a valid IP address"

# Input from user
user_input = input("Enter something: ").strip()
result = check_ip(user_input)
print(result)
