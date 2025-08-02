"""
 Find all files in the current folder (and subfolders)
 that use American-style dates in their names (MM-DD-YYYY)
 and rename them to European-style (DD-MM-YYYY)
 """
import os, re, shutil

# MM-DD-YYYY pattern
date_pattern = re.compile(r"""
    ^(.*?)             # All text before the date
    (\d{2})-           # Month
    (\d{2})-           # Day
    (\d{4})            # Year
    (.*?)$             # All text after the date
    """, re.VERBOSE)

def rename_dates(folder):
    folder = os.path.abspath(folder)

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            mo = date_pattern.search(filename)
            if not mo:
                continue # Skip files without a pattern

            before_part = mo.group(1)
            month = mo.group(2)
            day = mo.group(3)
            year = mo.group(4)
            after_part = mo.group(5)

            euro_filename = f'{before_part}{day}-{month}-{year}-{after_part}'
            old_path = os.path.join(foldername, filenames)
            new_path = os.path.join(foldername, euro_filename)

# Example usage
rename_dates('folder_with_us_dates')
