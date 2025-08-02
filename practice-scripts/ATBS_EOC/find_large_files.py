# Walk through a folder tree and print the absolute paths of all files larger than 100MB
import os

def find_large_files(folder, size_limit_mb=100):
    folder = os.path.abspath(folder)
    size_limit = size_limit_mb * 1024 * 1024 # Covert MB to bytes

    print(f'Scanning for files larger than {size_limit_mb}MB in {folder}...')

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            full_path = os.path.join(foldername, filename)
            try:
                if os.path.getsize(full_path) > size_limit:
                    print(f'{full_path} - {round(os.path.getsize(full_path) / (1024*1024), 2)} MB')
            except OSError as e:
                print(f'Error accessing {full_path}: {e}')

# Example usage:
find_large_files('folder_to_scan')
