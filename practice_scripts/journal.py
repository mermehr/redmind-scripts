#!/usr/bin/env python3
# Simple script to copy a templated file, inserts date and moves and renames the new file.
import os
from datetime import datetime
import subprocess

# Paths
template_path = os.path.expanduser("~< Path to template >")
output_dir = os.path.expanduser("< New file directory >")

# Get current date formats
today = datetime.now()
date_str_filename = today.strftime("%Y-%m-%d")  # For filename
date_str_formatted = today.strftime("%A %dth, %B %dth, %Y")  # Display format with 'th'

# File paths
output_path = os.path.join(output_dir, f"{date_str_filename}.md")

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# If file exists, just open it
if os.path.exists(output_path):
    subprocess.run(["xed", output_path])
else:
    # Read template
    with open(template_path, "r") as f:
        content = f.read()

    # Replace the {{date:...}} placeholder with formatted date
    content = content.replace("{{date:dddd, MMMM Do, YYYY}}", date_str_formatted)

    # Write new file
    with open(output_path, "w") as f:
        f.write(content)

    # Open with xed
    subprocess.run(["xed", output_path])
