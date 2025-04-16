import socket
import ipaddress
import concurrent.futures

# Define a list of common ports to scan.
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

def scan_port(ip, port, timeout=1):
    """
    Try to connect to the given IP and port.
    Returns True if the port is open, otherwise False.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        if s.connect_ex((str(ip), port)) == 0:
            return True
    except Exception:
        return False
    finally:
        s.close()
    return False

def scan_ip(ip):
    """
    Scans a single IP address for open common ports.
    Returns a list of open ports for that IP.
    """
    open_ports = []
    for port in COMMON_PORTS:
        if scan_port(ip, port):
            open_ports.append(port)
    return open_ports

def main():
    print("Welcome to the Local Network Port Scanner!")
    # Prompt user for a target network in CIDR format (e.g., "192.168.1.0/24")
    target_network = input("Enter target network (e.g., 192.168.1.0/24): ").strip()
    
    try:
        network = ipaddress.ip_network(target_network, strict=False)
    except ValueError as e:
        print("Invalid network address provided.")
        return

    print(f"Scanning network: {network}")
    results = {}  # Dictionary to store IPs with their open ports.

    # Use a thread pool to scan IPs concurrently (improves speed on larger networks).
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_to_ip = {executor.submit(scan_ip, ip): ip for ip in network.hosts()}
        for future in concurrent.futures.as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                open_ports = future.result()
                if open_ports:
                    results[str(ip)] = open_ports
                    print(f"IP: {ip}  Open ports: {open_ports}")
            except Exception as exc:
                print(f"Error scanning IP {ip}: {exc}")

    # Save scanning results to a log file.
    log_file = "scan_results.txt"
    with open(log_file, "w") as log:
        for ip, ports in results.items():
            log.write(f"{ip}: {ports}\n")
    print(f"Scan complete. Results saved to '{log_file}'.")

if __name__ == "__main__":
    main()
