"""
Find all files in a folder with a given prefix (like spam001.txt, spam002.txt...),
detect any numbering gaps, and rename later files to close those gaps
"""
import os, re

def renumber_files(folder, prefix, extension):
    folder = os.path.abspath(folder)
    file_pattern = re.compile(rf'{re.escape(prefix)}(\d{{3}}){re.escape(extension)}$')

    files = []
    for filename in os.listdir(folder):
        mo = file_pattern.match(filename)
        if mo:
            files.append((int(mo.group(1)), filename))

    files.sort() # Sort by number
    next_number = 1

    for number, filename in files:
        expected_filename = f'{prefix}{str(next_number).zfill(3)}{extension}'
        if filename != expected_filename:
            print(f'Renaming {filename} -> {expected_filename}')
            src = os.path.join(folder, filename)
            dst = os.path.join(folder, expected_filename)
            os.rename(src, dst)
        next_number += 1

# Uncomment to generate test files:
"""
for i in range(1, 121):
    if i not in (42, 86, 103):
        with open(f'spam{str(i).zfill(3)}.txt', 'w') as file:
            pass
"""

# Example usage
renumber_files('folder_with_files', 'spam', '.txt')