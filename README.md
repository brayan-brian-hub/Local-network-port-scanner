# Local Network Port Scanner

This Python tool scans a specified IP network range (CIDR notation) for common open ports. It uses multi-threading to efficiently scan multiple hosts concurrently and logs any open ports found.

## 🔥 What It's Used For

This tool is designed for:
- **Network Assessment:** Identify open ports on your own or authorized networks.
- **Educational Purposes:** Learn how common port scanning works and understand basic network security vulnerabilities.
- **Security Testing:** Assess the security posture of a network (with proper authorization).

## ⚠️ Responsible Use Notice

**DISCLAIMER:**  
This tool is for educational purposes only. It is intended to be used on networks you own or have explicit permission to scan. Unauthorized scanning is illegal and unethical. Use this tool responsibly.

## Features

- Scans a user-specified network range (e.g., 192.168.1.0/24)
- Checks common ports (e.g., 21, 22, 23, 80, 443, etc.)
- Multi-threaded scanning for speed and efficiency
- Saves results to a file (`scan_results.txt`)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/brayan-brian-hub/local-network-port-scanner.git
   cd local-network-port-scanner
2. Run the script:
   python network_scanner.py
3. Enter the target network in CIDR notation when prompted.

Requirements
   Python 3.x

