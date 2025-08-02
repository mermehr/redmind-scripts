#!/usr/bin/python
# A simple script to restructure a folders files.

import os
import shutil
import fnmatch

# Set to the root of the cloned repo
repo_root = "./<repo>"
count = 0

for root, dirs, files in os.walk(repo_root):
    # Match folders like part01/part01-*/src
    if fnmatch.fnmatch(root, "*/part*/part*/*"):
        print(f"[+] Found matching src folder: {root}")

        for file in files:
            if file.endswith(".py"):
                src_path = os.path.join(root, file)
                
                # Calculate ../../ from src/ = goes back to partXX/
                dest_dir = os.path.abspath(os.path.join(root, "..", ".."))
                dest_path = os.path.join(dest_dir, file)

                # Avoid overwriting
                if os.path.exists(dest_path):
                    print(f"[!] Skipping (already exists): {dest_path}")
                    continue

                print(f"[→] Copying {file} → {dest_dir}")
                shutil.copy2(src_path, dest_path)
                count += 1

print(f"[✓] Extraction complete! {count} files copied.")