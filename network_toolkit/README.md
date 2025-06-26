# Python Network & Security CLI Toolkit

A modular command-line toolkit for basic network security tasks, built in Python. Ideal for SOC analysts, ethical hackers, and learners in the networking field.

## Features

| Tool       | Description                                      |
|------------|--------------------------------------------------|
| `portscan` | TCP Port scanner using socket module             |
| `sniffer`  | Packet sniffer using Scapy                       |
| `dns`      | Simple DNS forward lookup                        |
| `httplog`  | Logs HTTP request and response headers           |
| `discover` | ARP scan for devices on local network (L2)       |

## Dependencies

pip install scapy colorama requests

## Usage Examples

python network_toolkit.py portscan --target 192.168.1.1 --ports 20-100" \
python network_toolkit.py sniffer --count 5 \
python network_toolkit.py dns --target example.com \
python network_toolkit.py httplog --target https://httpbin.org/get \
python network_toolkit.py discover --target 192.168.1.0/24

## Output to File

Use --output to save results:

python network_toolkit.py dns --target example.com --output results/dns_log.txt
