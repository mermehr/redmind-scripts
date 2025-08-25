#!/bin/bash

# Usage: ./deep_recon.sh <target-ip>
# Example: ./deep_recon.sh 192.168.56.101

TARGET="$1"
OUTPUT_DIR="scan_$TARGET"
# Change when needed
WORDLIST="/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
# Colors
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
CYAN="\033[0;36m"
RESET="\033[0m"

if [ -z "$TARGET" ]; then
    echo "Usage: $0 <target-ip>"
    exit 1
fi

echo -e "${CYAN}[*] Starting Deep Recon on $TARGET...${RESET}"
mkdir -p "$OUTPUT_DIR"

# Nmap deep scan (version, script, full port range)
echo -e "${CYAN}[*] Running Nmap full scan...${RESET}"
nmap -sV -sC --min-rate 500 -oN "$OUTPUT_DIR/nmap_output.txt" "$TARGET"

# Find HTTP port (look for lines with 'http' service)
HTTP_LINE=$(grep -iE '^[0-9]+/tcp\s+open\s+http' "$OUTPUT_DIR/nmap_output.txt" | head -n 1)
HTTP_PORT=$(echo "$HTTP_LINE" | cut -d '/' -f1)

if [ -z "$HTTP_PORT" ]; then
    echo -e "${YELLOW}[!] No obvious HTTP port found in Nmap results. Skipping Gobuster.${RESET}"
else
    # Check for https service
    if echo "$HTTP_LINE" | grep -iq 'https'; then
        PROTOCOL="https"
    else
        PROTOCOL="http"
    fi

    echo -e "${CYAN}[*] Running Gobuster on $PROTOCOL://$TARGET:$HTTP_PORT ...${RESET}"
    gobuster dir -u "$PROTOCOL://$TARGET:$HTTP_PORT" -w "$WORDLIST" -o "$OUTPUT_DIR/gobuster_output.txt"
fi

# Step 3: Run the Python parser script
echo "[*] Parsing results..."
python3 recon_parser.py "$OUTPUT_DIR/nmap_output.txt" "$OUTPUT_DIR/gobuster_output.txt"

echo "[*] Recon complete. Results saved in $OUTPUT_DIR/"