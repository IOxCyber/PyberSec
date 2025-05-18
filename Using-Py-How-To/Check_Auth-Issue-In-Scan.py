# To Check Auth Based IP Scan: Port & Running Services, OS type

# vm_scanner.py for Auth Isuue in IP Based Scans.

import subprocess
import ipaddress

# ======================[ Validation Module ]======================

def is_valid_ip(ip: str) -> bool:
    """Validate if the provided string is a valid IPv4 or IPv6 address."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


# =======================[ Discovery Module ]======================

def is_host_alive(ip: str) -> bool:
    """Check if the host is alive using various Nmap probe types."""
    try:
        print(f"🔍 Checking if host {ip} is alive...")
        result = subprocess.run(
            ['nmap', '-sn', '-PA21,22,80,443', '-PE', '-PP', '-PR', '-T4', ip],
            capture_output=True, text=True
        )
        if "Host is up" in result.stdout:
            print(f" Host {ip} is alive.\n")
            return True
        else:
            print(f"❌ Host {ip} is not responding to discovery probes.")
            return False
    except Exception as e:
        print(f"[!] Error during host discovery: {e}")
        return False


# =======================[ Scan Modules ]==========================

def run_nmap_script(ip: str, ports: str, scripts: str) -> str:
    """Run a specific Nmap script on given ports."""
    try:
        command = ['nmap', '-p', ports, '--script', scripts, ip]
        return subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        return f"[!] Nmap script scan failed:\n{e.output}"


def detect_os(ip: str) -> str:
    """Perform OS detection using Nmap."""
    try:
        return subprocess.check_output(['nmap', '-O', ip], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        return f"[!] OS detection failed:\n{e.output}"


# =======================[ Reporting Module ]======================

def summarize_results(ip, ssh, smb2, smb1, os_data):
    """Print formatted summary of scan results."""
    print("\n" + "="*40)
    print(f" Scan Summary for {ip}")
    print("="*40)

    # SSH
    if "OpenSSH" in ssh or "ssh-" in ssh:
        print("[✔] SSH detected on port 22.")
    elif "22/tcp open" in ssh:
        print("[⚠] Port 22 is open, but no SSH banner detected.")
    else:
        print("[✖] Port 22 not open.")

    # SMBv2/v3
    if "SMBv2" in smb2 or "SMBv3" in smb2:
        print("[✔] SMBv2/SMBv3 detected on port 445.")
    elif "445/tcp open" in smb2:
        print("[⚠] Port 445 open, SMB version undetermined.")
    else:
        print("[✖] Port 445 not open.")

    # SMBv1
    if "SMBv1" in smb1 or "vulnerable" in smb1:
        print("[⚠] SMBv1 detected or service vulnerable on port 139.")
    elif "139/tcp open" in smb1:
        print("[✔] Port 139 open, SMBv1 not detected.")
    else:
        print("[✖] Port 139 not open.")

    # OS
    print("\n OS Detection Guess:")
    detected = False
    for line in os_data.splitlines():
        if any(keyword in line for keyword in ["OS details", "Running", "Device type", "Aggressive OS guesses"]):
            print("   →", line.strip())
            detected = True
    if not detected:
        print("   → No OS details detected.")


# =======================[ Main Logic ]======================

def main():
    ip = input("Enter a valid IP address: ").strip()

    if not is_valid_ip(ip):
        print(" Invalid IP address format.")
        return

    if not is_host_alive(ip):
        print("Host is not alive. Skipping scan.")
        return

    print("\n[+] Starting Targeted Service & OS Scan...")

    ssh_result = run_nmap_script(ip, "22", "ssh-hostkey")
    smb2_result = run_nmap_script(ip, "445", "smb-protocols")
    smb1_result = run_nmap_script(ip, "139", "smb-vuln*")
    os_result = detect_os(ip)

    summarize_results(ip, ssh_result, smb2_result, smb1_result, os_result)


if __name__ == "__main__":
    main()
