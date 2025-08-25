#!/usr/bin/python
import argparse
import socket
import requests
from pathlib import Path
from datetime import datetime

try:
    from scapy.all import sniff, ARP, Ether, srp
except ImportError:
    print("[!] Scapy is not installed. Run: pip install scapy")
    exit(1)

try:
    from colorama import Fore, Style, init
    init()
except ImportError:
    print("[!] Colorama is not installed. Run: pip install colorama")
    exit(1)


def write_output(output, file_path=None):
    print(output)
    if file_path:
        with open(file_path, 'a') as f:
            f.write(output + '\n')


def scan_ports(host, ports, output_file=None):
    for port in ports:
        with socket.socket() as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            status = f"{Fore.GREEN}Open{Style.RESET_ALL}" if result == 0 else f"{Fore.RED}Closed{Style.RESET_ALL}"
            write_output(f"Port {port}: {status}", output_file)


def packet_callback(pkt):
    print(pkt.summary())


def dns_lookup(domain, output_file=None):
    try:
        ip = socket.gethostbyname(domain)
        write_output(f"{Fore.CYAN}{domain} → {ip}{Style.RESET_ALL}", output_file)
    except Exception as e:
        write_output(f"{Fore.RED}[!] DNS error: {e}{Style.RESET_ALL}", output_file)


def log_request(url, output_file=None):
    try:
        resp = requests.get(url)
        headers_out = "\n[Request Headers]:\n" + "\n".join(f"{k}: {v}" for k, v in resp.request.headers.items())
        headers_out += "\n\n[Response Headers]:\n" + "\n".join(f"{k}: {v}" for k, v in resp.headers.items())
        write_output(f"{Fore.YELLOW}{headers_out}{Style.RESET_ALL}", output_file)
    except Exception as e:
        write_output(f"{Fore.RED}[!] Request failed: {e}{Style.RESET_ALL}", output_file)


def arp_scan(network, output_file=None):
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    ans = srp(ether / arp, timeout=2, verbose=False)[0]
    write_output(f"{Fore.MAGENTA}\n[Discovered Devices]:{Style.RESET_ALL}", output_file)
    for _, rcv in ans:
        write_output(f"{rcv.psrc} → {rcv.hwsrc}", output_file)


def main():
    parser = argparse.ArgumentParser(description="Python Network & Security CLI Toolkit")
    parser.add_argument("tool", choices=["portscan", "sniffer", "dns", "httplog", "discover"],
                        help="Choose which tool to run")
    parser.add_argument("--target", help="Target IP/domain/subnet")
    parser.add_argument("--ports", help="Port range (start-end) for port scanning", default="1-1024")
    parser.add_argument("--count", help="Packet count for sniffer", type=int, default=10)
    parser.add_argument("--output", help="Optional output file to save results")

    args = parser.parse_args()

    output_file = None
    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, 'w') as f:
            f.write(f"# Output - {datetime.now()}\n")
        output_file = args.output

    if args.tool == "portscan":
        if not args.target:
            print("[!] Port scan requires --target")
            return
        start, end = map(int, args.ports.split("-"))
        scan_ports(args.target, range(start, end + 1), output_file)

    elif args.tool == "sniffer":
        sniff(count=args.count, prn=packet_callback)

    elif args.tool == "dns":
        if not args.target:
            print("[!] DNS lookup requires --target (domain)")
            return
        dns_lookup(args.target, output_file)

    elif args.tool == "httplog":
        if not args.target:
            print("[!] HTTP logger requires --target (URL)")
            return
        log_request(args.target, output_file)

    elif args.tool == "discover":
        if not args.target:
            print("[!] Network discovery requires --target (CIDR subnet)")
            return
        arp_scan(args.target, output_file)


if __name__ == "__main__":
    main()