# Python Network Sniffer & UDP/ICMP Scanner

This repo contains two small Python 3 tools adapted from *Black Hat Python, 2nd Edition* and cleaned up for direct use in a lab environment. Both rely on raw sockets, so **root/admin privileges are required**.

------------------------------------------------------------------------

## Scripts

### 1. `icmp_sniffer.py`

A minimal ICMP sniffer that parses IP headers and ICMP headers from captured packets.

-   Prints out:
    -   Source and destination addresses
    -   Protocol
    -   IP version, header length, TTL
    -   ICMP type and code

**Usage:**

``` bash
# Linux/macOS (requires sudo)
sudo python3 icmp_sniffer.py 0.0.0.0

# Windows (run as admin, bind to your local IP)
python icmp_sniffer.py 192.168.56.1
```

------------------------------------------------------------------------

### 2. `udp_icmp_scanner.py`

A UDP spray and ICMP response sniffer that discovers live hosts by sending UDP packets containing a magic payload across a subnet, then listening for ICMP Type 3 / Code 3 (Port Unreachable) replies.

-   **Default subnet:** `192.168.56.0/24`\
-   **Magic string:** `DoNoT3tHi$`\
-   **Destination port:** `65212`

Hosts that respond with an ICMP error containing the magic string are reported as up.

**Usage:**

``` bash
# Linux/macOS (requires sudo)
sudo python3 udp_icmp_scanner.py 0.0.0.0

# Windows (run as admin, bind to your local IP)
python udp_icmp_scanner.py 192.168.56.1
```

------------------------------------------------------------------------

## Requirements

-   Python 3.6+
-   Root or Administrator privileges
-   Raw sockets enabled
-   For Windows: run from an elevated prompt to allow `SIO_RCVALL`

------------------------------------------------------------------------

## Notes

-   These are intended for **lab/test environments** only.
-   Behavior may differ slightly across OSes:
    -   On Linux/macOS, raw sockets are bound with `IPPROTO_ICMP`.
    -   On Windows, `IPPROTO_IP` is used and promiscuous mode is enabled
        with `SIO_RCVALL`.

------------------------------------------------------------------------

## Disclaimer

These tools are provided for **educational and research purposes** in controlled environments.
Do not use them on networks you do not own or have explicit permission to test.
