"""
Walk through a folder tree and copy all files with a specific
extension (e.g., .pdf, .jpg) to a new destination folder.
"""

import os, shutil

def selective_copy(src_folder, dest_folder, extension):
    src_folder = os.path.abspath(src_folder)
    dest_folder = os.path.abspath(dest_folder)

    print(f'Searching for *{extension} files in {src_folder}...')

    for foldername, subfolders, filenames in os.walk(src_folder):
        for filename in filenames:
            if filename.endswith(extension):
                full_path = os.path.join(foldername, filename)
                print(f'Found: {full_path}')

                os.makedirs(dest_folder, exist_ok=True)
                shutil.copy(full_path, dest_folder)
                print(f'Copied to: {dest_folder}')

# Example usage
selective_copy('source', 'destination', '.pdf')