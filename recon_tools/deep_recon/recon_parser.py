#!/usr/bin/env python3
import sys
import re

# ANSI color codes
RESET = '\033[0m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
MAGENTA = '\033[35m'

def parse_nmap(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    ips = []
    ports = []
    os_info = []

    for line in lines:
        if "Nmap scan report for" in line:
            match = re.search(r'Nmap scan report for (\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ips.append(match.group(1))

        if re.match(r'^\d+/tcp\s+open', line):
            parts = line.strip().split()
            port = parts[0].split('/')[0]
            service = parts[2]
            version = ' '.join(parts[3:]) if len(parts) > 3 else ''
            ports.append((port, service, version))

        if "OS details:" in line or "Aggressive OS guesses:" in line or "Running:" in line:
            os_info.append(line.strip())

    return ips, ports, os_info

def parse_gobuster(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        endpoints = re.findall(r'(/\S+)\s+\(Status:\s+\d+', data)
        return endpoints
    except FileNotFoundError:
        return []

def main():
    if len(sys.argv) != 3:
        print("Usage: python recon_parser.py <nmap_output.txt> <gobuster_output.txt>")
        return

    nmap_file = sys.argv[1]
    gobuster_file = sys.argv[2]

    ips, ports, os_info = parse_nmap(nmap_file)
    endpoints = parse_gobuster(gobuster_file)

    target_id = ips[0] if ips else "unknown"
    output_file = f"{target_id}.txt"

    with open(output_file, 'w') as out:

        # IPs
        print(CYAN + "\n[+] IP Addresses Found:" + RESET)
        out.write("[+] IP Addresses Found:\n")
        for ip in ips:
            print(GREEN + f"  - {ip}" + RESET)
            out.write(f"  - {ip}\n")

        # Ports
        print(CYAN + "\n[+] Open Ports with Service Info:" + RESET)
        out.write("\n[+] Open Ports with Service Info:\n")
        for port, service, version in ports:
            print(YELLOW + f"  - Port: {port} | Service: {service} | Version: {version}" + RESET)
            out.write(f"  - Port: {port} | Service: {service} | Version: {version}\n")

        # OS Fingerprint
        if os_info:
            print(CYAN + "\n[+] OS Fingerprint Info:" + RESET)
            out.write("\n[+] OS Fingerprint Info:\n")
            for line in os_info:
                print(f"  {line}")
                out.write(f"  {line}\n")

        # HTTP Endpoints
        print(CYAN + "\n[+] HTTP Endpoints Found:" + RESET)
        out.write("\n[+] HTTP Endpoints Found:\n")
        for endpoint in endpoints:
            print(MAGENTA + f"  - {endpoint}" + RESET)
            out.write(f"  - {endpoint}\n")

    print(GREEN + f"\n[+] Output written to {output_file}" + RESET)

if __name__ == "__main__":
    main()
