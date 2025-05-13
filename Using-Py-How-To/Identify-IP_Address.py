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

while True:
    # Input from user
    user_input = input("Enter an IP address: ").strip()
    result = check_ip(user_input)
    print(result)
    
    # Ask user if they want to continue
    choice = input("Do you want to check another IP? (Y/N): ").strip().lower()
    if choice != 'y':
        print("Exiting, Bye!")
        break
