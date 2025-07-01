#!/bin/bash

# get-kali-tool.sh — Smart tool installer for Linux Mint with Kali + GitHub/Flatpak fallback

# This will attempt to pull a kali package from their repo if one is not available in Mint's
# It will fallback to check flatpak and the build from git if available
# WARNING - will overwrite system deps if not carefull

KALI_REPO_FILE="/etc/apt/sources.list.d/kali.list"
KALI_KEYRING="/etc/apt/trusted.gpg.d/kali-keyring-2025.gpg"

# Color codes
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
NC="\033[0m"

# Check for root
if [[ "$EUID" -ne 0 ]]; then
  echo -e "${RED}Please run as root.${NC}"
  exit 1
fi

# Check for input
if [[ -z "$1" ]]; then
  echo -e "${YELLOW}Usage:${NC} $0 <tool-name>"
  exit 1
fi

TOOL="$1"

echo -e "${GREEN}[+] Checking if '$TOOL' is in Mint repo...${NC}"
if apt-cache show "$TOOL" 2>/dev/null | grep -q '^Package: '; then
  echo -e "${GREEN}[✓] Found in Mint repo. Installing...${NC}"
  apt install -y "$TOOL"
  exit $?
else
  echo -e "${YELLOW}[!] Not found in Mint repo. Trying Kali repo...${NC}"
fi

echo -e "${YELLOW}[!] Not found in Mint repo. Trying Kali repo...${NC}"

# Enable Kali repo temporarily
echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > "$KALI_REPO_FILE"

# Confirm Kali keyring is present
if [[ -f "$KALI_KEYRING" ]]; then
  echo -e "${GREEN}[+] Kali GPG key already present at $KALI_KEYRING${NC}"
else
  echo -e "${YELLOW}[!] Kali key not found — fetching it...${NC}"
  wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add -
fi

# Only update from Kali repo without affecting Mint's sources
apt update -o Dir::Etc::sourcelist="$KALI_REPO_FILE" -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"

echo -e "${GREEN}[+] Checking if '$TOOL' is in Kali repo...${NC}"
apt-cache policy "$TOOL" | grep -q 'Candidate: (none)'
IN_KALI=$?

echo -e "${YELLOW}[!] '$TOOL' found in Kali repo, but be cautious.${NC}"
read -rp "$(echo -e ${YELLOW}[?] Install '$TOOL' from Kali with minimal dependencies? "(y/n): "${NC})" CONFIRM_KALI
if [[ "$CONFIRM_KALI" =~ ^[Yy]$ ]]; then
  echo -e "${GREEN}[+] Installing with --no-install-recommends...${NC}"
  apt install --no-install-recommends -t kali-rolling "$TOOL"
else
  echo -e "${YELLOW}[-] Skipping Kali install.${NC}"
fi

echo -e "${RED}[×] '$TOOL' not found in Kali either.${NC}"
rm "$KALI_REPO_FILE"
apt update

# Prompt user for fallback
read -rp "$(echo -e ${YELLOW}"[?] Try to clone '$TOOL' from GitHub, skip, or search for a Flatpak? (y/n/f): "${NC})" CHOICE
if [[ "$CHOICE" =~ ^[Yy]$ ]]; then
  GH_REPO="https://github.com/$(echo "$TOOL" | tr '[:upper:]' '[:lower:]')/$TOOL.git"
  echo -e "${GREEN}[+] Attempting to clone ${GH_REPO}...${NC}"
  git clone "$GH_REPO" /opt/"$TOOL" && echo -e "${GREEN}[✓] Cloned to /opt/$TOOL${NC}" || echo -e "${RED}[×] Clone failed.${NC}"
elif [[ "$CHOICE" =~ ^[Ff]$ ]]; then
  echo -e "${YELLOW}[*] Opening browser to search for Flatpak...${NC}"
  xdg-open "https://flathub.org/apps/search/$TOOL" >/dev/null 2>&1 &
else
  echo -e "${YELLOW}[-] Skipping fallback step.${NC}"
fi