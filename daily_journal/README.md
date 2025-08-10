# Daily Journal

This folder contains a reusable **daily journal template** (`daily.md`) and a Python helper script that generates dated entries from it.

## Structure

```
daily-journal/
├── daily_template.md                 # Template file for new journal entries
├── daily_journal.py         # Python script to create/open daily entries
└── daily/
    └── YYYY-MM-DD.md
    └── ...        
```

## Template

The template file `daily.md` contains the base layout for each daily entry, including a placeholder for the current date:

```markdown
## Daily Journal - {{date:dddd, MMMM Do, YYYY}}

**Focus Areas**: [Python, Red Team, HTB]

---
...etc...
```

When the script runs, it adds `{{date:dddd, MMMM Do, YYYY}}` with the current date in a format like:

```
Sunday, August 10th, 2025
```

## Script Features

- Reads `daily.md` from the repository root.
- Inserts the current date (with proper ordinal suffixes).
- Saves the result to `daily/YYYY-MM-DD.md`.
- If the file already exists for today, it **does not overwrite** it.
- Opens the created/existing file in **xed** (or your default text editor).

## Installation & Requirements

### System Requirements
- **OS:** Linux Mint/Ubuntu (tested on Mint 22.1)
- **Python:** Version 3.8+
- **Editor:** `xed` (Linux Mint default text editor)

### Required System Packages
To ensure `xed` can load its Python plugins without errors, install the following:
```bash
sudo apt update
sudo apt install -y python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-glib-2.0 libpeas-1.0-0 gir1.2-peas-1.0 xed
```

### Python Environment
No additional Python packages are required; the script uses only the Python standard library.

## Usage

1. Make the script executable:
   ```bash
   chmod +x daily_journal.py
   ```
2. Run the script:
   ```bash
   ./daily_journal.py
   ```
   This will create/open today’s journal entry in `ldaily/`.

## Notes

- The script strips Python environment variables before launching `xed` to avoid PyGObject/libpeas errors caused by pyenv or virtual environments.
- You can edit `daily.md` to change the layout or fields for future entries.
- Existing entries are **never** overwritten; to edit a past day, just open the corresponding file in `daily/`.

---
