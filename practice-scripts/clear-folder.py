#!/usr/bin/python
# A simple script to clear a working folder while keeping some files intact.

import os
import shutil

target_dir = "../file-ops/"
trash_extensions = [".nmap", ".xml", ".txt", ".html"]
trash_dirs = ["gobuster", "ffuf-output", "nmap-temp", "temp",]
DRY_RUN = True  # Flip to False when ready

if not os.path.isdir(target_dir):
    print(f"[!] Folder not found: {target_dir}")
    exit()

for item in os.listdir(target_dir):
    full_path = os.path.join(target_dir, item)

    if os.path.isfile(full_path):
        _, ext = os.path.splitext(item)
        if ext.lower() in trash_extensions:
            if DRY_RUN:
                print(f"[DRY RUN] Would delete file: {item}")
            else:
                print(f"[x] Deleting file: {item}")
                os.remove(full_path)

    elif os.path.isdir(full_path):
        if item in trash_dirs or item.startswith("scan_"):
            if DRY_RUN:
                print(f"[DRY RUN] Would remove folder: {item}")
            else:
                print(f"[x] Removing folder: {item}")
                shutil.rmtree(full_path)

print("[✓] Cleanup complete.")
