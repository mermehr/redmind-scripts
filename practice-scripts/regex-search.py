import os
import re

# Banner
def print_banner():
    banner = r"""
 _____            _             _____                          
|  __ \          | |           / ____|                         
| |__) |___   ___| | _____ _ _| (___   ___ _ ____   _____ _ __ 
|  _  // _ \ / __| |/ / _ \ '__\___ \ / _ \ '__\ \ / / _ \ '__|
| | \ \ (_) | (__|   <  __/ |  ____) |  __/ |   \ V /  __/ |   
|_|  \_\___/ \___|_|\_\___|_| |_____/ \___|_|    \_/ \___|_|   

Regex Search Tool – Practice Edition 
    """
    print(banner)

# Tooltip
def print_tooltip():
    tooltip = """
💡 Enter a valid regular expression to search all `.txt` files in the specified folder.
Examples:
    - \\bcat\\b            → Match the exact word 'cat'
    - \\d{3}-\\d{3}-\\d{4} → Match phone numbers like 123-456-7890
    - ^ERROR               → Match lines that start with 'ERROR'
    - [A-Z]{3,}            → Match 3 or more capital letters in a row  
    """
    print(tooltip)

# Search function
def regex_search_in_txt_files(folder_path, regex_pattern):
    try:
        regex = re.compile(regex_pattern)
    except re.error as e:
        print(f"Invalid regex pattern: {e}")
        return

    if not os.path.isdir(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    print(f"\nSearching for pattern: '{regex_pattern}'")
    print(f"In folder: {folder_path}\n")

    match_found = False
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    for line_num, line in enumerate(file, start=1):
                        if regex.search(line):
                            print(f"[{filename} - Line {line_num}]: {line.strip()}")
                            match_found = True
            except Exception as e:
                print(f"Could not read {filename}: {e}")
    if not match_found:
        print("Search complete. No matches found.")

if __name__ == "__main__":
    print_banner()
    print_tooltip()
    folder = input("Enter folder path to search in: ").strip()
    pattern = input("Enter your regular expression: ").strip()
    regex_search_in_txt_files(folder, pattern)

