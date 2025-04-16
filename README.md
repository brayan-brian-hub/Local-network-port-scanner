# Local Network Port Scanner

This Python tool scans a specified IP network range (CIDR notation) for common open ports. It uses multi-threading to efficiently scan multiple hosts concurrently and logs any open ports found. This project is ideal for educational purposes and demonstrates how to build a basic cybersecurity scanner.

## Features

- Scans a user-specified network range (e.g., 192.168.1.0/24)
- Checks for common ports like 21, 22, 23, 80, 443, etc.
- Multi-threaded scanning for speed and efficiency
- Logs results to a file (`scan_results.txt`)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/brayan-brian-hub/network-scanner.git
   cd network-scanner

2. Run the script:
    python network_scanner.py
3. Enter the network range in CIDR notation when prompted (e.g., 192.168.1.0/24).
   Results will be displayed in the console and saved in scan_results.txt.

