import subprocess
import ipaddress

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def scan_ip(ip):
    print(f"\n[*] Scanning IP: {ip} for OS and open ports...\n")
    # Use Nmap with OS detection (-O) and common ports scan
    try:
        result = subprocess.check_output(['nmap', '-O', ip], stderr=subprocess.STDOUT, text=True) #check_output(..) function will execute cmd ie nmap -O in CLI
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")

# Main
user_ip = input("Enter an IP address: ").strip()

if is_valid_ip(user_ip):
    scan_ip(user_ip)
else:
    print("Invalid IP address. Please enter a valid IPv4 or IPv6.")
