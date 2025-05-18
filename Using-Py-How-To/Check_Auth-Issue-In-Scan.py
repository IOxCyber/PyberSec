# To Check Auth Based IP Scan: Port & Running Services, OS type

import subprocess
import ipaddress

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def run_nmap_script(ip, ports, scripts):
    try:
        command = ['nmap', '-p', ports, '--script', scripts, ip]
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"[!] Nmap script scan failed:\n{e.output}"

def os_detection(ip):
    try:
        result = subprocess.check_output(['nmap', '-O', ip], stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"[!] OS Detection Failed:\n{e.output}"

def main():
    ip = input("Enter a valid IP address: ").strip()

    if not is_valid_ip(ip):
        print("Invalid IP! Please enter a valid IPv4 or IPv6.")
        return

    print("\n[+] Scanning IP:", ip)

    print("\n[*] Checking if SSH is really running on port 22...")
    ssh_result = run_nmap_script(ip, "22", "ssh-hostkey")
    
    print("\n[*] Checking if SMBv2/v3 is running on port 445...")
    smb2_result = run_nmap_script(ip, "445", "smb-protocols")
    
    print("\n[*] Checking if SMBv1 is detected on port 139...")
    smb1_result = run_nmap_script(ip, "139", "smb-vuln*")
    
    print("\n[*] Performing OS Detection...")
    os_result = os_detection(ip)

    # === Summary Parser ===
    print("\n" + "="*40)
    print("Scan Summary Report")
    print("="*40)

    if "OpenSSH" in ssh_result or "ssh-" in ssh_result:
        print("[✔] SSH detected on port 22.")
    elif "22/tcp open" in ssh_result:
        print("[⚠] Port 22 is open, but no SSH banner detected.")
    else:
        print("[✖] Port 22 not open.")

    if "SMBv2" in smb2_result or "SMBv3" in smb2_result:
        print("[✔] SMBv2/SMBv3 detected on port 445.")
    elif "445/tcp open" in smb2_result:
        print("[⚠] Port 445 open, but SMBv2/3 not confirmed.")
    else:
        print("[✖] Port 445 not open.")

    if "SMBv1" in smb1_result or "vulnerable" in smb1_result:
        print("[⚠] SMBv1 detected or vulnerable service on port 139!")
    elif "139/tcp open" in smb1_result:
        print("[✔] Port 139 open, no SMBv1 detected.")
    else:
        print("[✖] Port 139 not open.")

    print("\n OS Detection Guess:")
    for line in os_result.splitlines():
        if "OS details" in line or "Running" in line:
            print("   →", line.strip())
    print("="*40)

if __name__ == "__main__":
    main()
