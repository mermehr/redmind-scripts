## Kali Tool Installer Script (`kali-tool.sh`)

This script provides a smart, semi-safe way to install Kali Linux tools on a Linux Mint (or other Debian-based) system without pulling the entire Kali environment. It attempts the following:

1. **Check Mint repos** for the tool
2. **Temporarily add Kali repo** to check/install the tool with `--no-install-recommends`
3. If still not found, optionally:
   - Clone from GitHub
   - Search Flatpak
   - Skip

---

### Warning

While some safety precautions are included (like using `--no-install-recommends`, prompting before Kali installs, and isolating `sources.list`), **this script may still overwrite system libraries or introduce broken dependencies** if a tool shares packages with critical system components.

> **DO NOT run this blindly on production systems or without reviewing the packages involved.**

Recommended for use on:
- **VMs**
- **Isolated labs**
- **Rebuildable environments**

---

### Usage

```bash
chmod +x kali-tool.sh
sudo ./kali-tool.sh <tool-name>