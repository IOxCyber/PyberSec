# ✅ Python Modules Every VM Automation Engineer Should Know

| Module          | Type              | What It Does                           | Use in VM Automation                                |
| --------------- | ----------------- | -------------------------------------- | --------------------------------------------------- |
| `ipaddress`     | Built-in          | IP validation & manipulation           | Validate scanned IPs, CIDRs, ranges                 |
| `subprocess`    | Built-in          | Run CLI tools (e.g., `nmap`, `qualys`) | Integrate system tools in your Python scripts       |
| `os`            | Built-in          | OS-level ops (env vars, path, etc.)    | Automate file handling, permissions                 |
| `socket`        | Built-in          | Network connections & DNS              | Port scanning, banner grabbing                      |
| `logging`       | Built-in          | Structured logs                        | Audit, debug scanning and patching workflows        |
| `json` / `yaml` | Built-in + PyYAML | Config parsing, API responses          | Parse config files, scan outputs, tool integrations |
| `re`            | Built-in          | Regex for parsing                      | Match CVE patterns, extract IPs/domains             |
| `csv`           | Built-in          | Read/write CSV reports                 | Automation with exported scan results               |
| `datetime`      | Built-in          | Time ops                               | Schedule scans, SLA checks                          |
| `argparse`      | Built-in          | CLI tools & arguments                  | Build security automation CLIs                      |
| `pathlib`       | Built-in          | Path ops                               | Safer file/directory handling                       |
| `shutil`        | Built-in          | Move, delete, copy files               | Rotate scan logs, manage backups                    |

---

# ☁️ External Modules (Install with `pip`) — Must-Haves

| Module                     | What It Does            | Usage                                                     |
| -------------------------- | ----------------------- | --------------------------------------------------------- |
| `requests`                 | HTTP requests           | Call scanner APIs (Qualys, Tenable, etc.)                 |
| `httpx`                    | Async HTTP client       | High-speed bulk API calls                                 |
| `paramiko`                 | SSH connections         | Remediate vulnerabilities over SSH                        |
| `netmiko`                  | SSH for network devices | Push configs to routers/switches                          |
| `pyvmomi`                  | VMware vSphere API      | VM lifecycle automation                                   |
| `openpyxl` / `pandas`      | Excel + data analysis   | Parse, clean vulnerability exports                        |
| `xml.etree.ElementTree`    | Parse XML               | Read Nessus/Qualys exports                                |
| `beautifulsoup4`           | HTML parsing            | Scrape reports or dashboards                              |
| `pynmap` / `python-nmap`   | Nmap integration        | Launch, parse Nmap scans from Python                      |
| `docker`                   | Docker SDK              | Security in containers                                    |
| `schedule`                 | Job scheduler           | Time-based automation (e.g., weekly scan trigger)         |
| `rich`                     | Pretty terminal output  | CLI dashboards and colorized reports                      |
| `tenable.io` / `qualysapi` | Vendor SDKs             | Direct API integration for asset scans, pulling vuln data |

---

# Real-World Automation Ideas Using These Modules

| Task                                         | Modules                               |
| -------------------------------------------- | ------------------------------------- |
| Validate scan scope before sending to Qualys | `ipaddress`, `socket`, `re`           |
| Auto-download and parse scan results         | `requests`, `json`, `csv`, `openpyxl` |
| Remediate vulnerabilities via SSH            | `paramiko`, `os`, `subprocess`        |
| Parse Nessus/Qualys XML/CSV                  | `xml`, `csv`, `pandas`                |
| Trigger scans via API + log the response     | `requests`, `logging`, `datetime`     |
| Schedule weekly report generation            | `schedule`, `os`, `openpyxl`, `rich`  |
| Filter IPs not scanned in 30 days            | `ipaddress`, `datetime`, `json`       |
| Check asset inventory against live Nmap      | `python-nmap`, `json`, `subprocess`   |

---

# 🧠 Bonus Tip: Grouping Modules by Function

| Function       | Modules                                        |
| -------------- | ---------------------------------------------- |
| **API**        | `requests`, `httpx`, `tenable.io`, `qualysapi` |
| **Network**    | `socket`, `ipaddress`, `pynmap`, `netmiko`     |
| **Automation** | `subprocess`, `schedule`, `argparse`           |
| **Parsing**    | `json`, `csv`, `yaml`, `xml`, `bs4`, `pandas`  |
| **System Ops** | `os`, `shutil`, `pathlib`, `logging`           |
| **SSH/Remote** | `paramiko`, `netmiko`                          |
| **VM/Infra**   | `pyvmomi`, `docker`, `libvirt-python`          |
