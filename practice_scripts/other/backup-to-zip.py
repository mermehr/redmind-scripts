"""
backup-to-zip.py - Copies an entire folder and its contents into
a ZIP file with filename incrementation
"""

import zipfile, os
from pathlib import Path

def backup_to_zip(folder):
    # Backup the entire contents of "folder" int a ZIP file
    folder = Path(folder) # Make sure the folder is the Path object, not string

    # Figure out the ZIP filename this code should use
    number = 1
    while True:
        zip_filename = Path(folder.parts[-1] + '_' + str(number) + '.zip')
        if not zip_filename.exists():
            break
        number = number +1

    # Create the ZIP file
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # Walk the entire folder tree and list the files in each folder
    for folder_name, subfolders, filenames in os.walk(folder):
        folder_name = Path(folder_name)
        print(f'Adding files in folder {folder_name}...')

        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            print(f'Adding file {filename}...')
            backup_zip.write(folder_name / filename)
    backup_zip.close()
    print('Done.')

backup_to_zip(Path.home() / 'spam')