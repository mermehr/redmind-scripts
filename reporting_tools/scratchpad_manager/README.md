# Scratchpad Manager

A simple **bash-based project scratchpad manager** for red team pentest workflow. Keeps projects organised, tracks the current active workspace with a symlink, and integrates screenshots directly into notes.

------------------------------------------------------------------------

## Features

-   Projects live under `~/scratchpad/<name>`

-   Active project symlink at `~/current`

-   Pre-populated structure:

        README.md
        notes.md
        TODO.md
        logs/commands.log
        assets/
        src/
        data/
        screens/

-   `flameshot` integration:

    -   Screenshots saved into `~/current/screens/`
    -   Automatically appended to `~/current/notes.md` as Markdown image
        links

------------------------------------------------------------------------

## Installation

1.  Save the script to `~/bin/scratchpad`:

    ``` bash
    chmod +x scratchpad.sh
    mv scratchpad.sh ~/bin/scratchpad
    ```

    (Make sure `~/bin` is in your `$PATH`.)

2.  Install [flameshot](https://flameshot.org/) if not already
    installed:

    ``` bash
    sudo apt install flameshot
    ```

------------------------------------------------------------------------

## Usage

``` bash
scratchpad <command> [options] [name]
```

### Commands

- `init <name>`
  
  Create new project under  `~/scratchpad/<name>` and point `~/current` to it.
  
- `init --force <name>`
  
  Reuse existing project directory if it  already exists.
  
- `init --no-relink <name>`
  
  Create project but do not update `~/current`.
  
- `link <name>`
  
  Point `~/current` to an existing project.
  
- `list` 
  
  List all projects under `~/scratchpad`  (marks the active one with `*`).
  
- `shot`  

  Take a screenshot with flameshot, save it in `~/current/screens/`, and append to `~/current/notes.md`.

------------------------------------------------------------------------

## Examples

``` bash
# create new project and activate it
scratchpad init htb-bashed

# list projects
scratchpad list
# output:
# htb-bashed *

# switch active project
scratchpad link filetransfer

# take screenshot into current project
scratchpad shot
# notes.md will now contain:
# ![screenshot](screens/20250826-0610.png)
```

------------------------------------------------------------------------

## Safety Notes

-   `~/current` is always a symlink.
    If a real directory exists at `~/current`, the script aborts with a
    warning.
-   Projects are never overwritten unless you explicitly pass `--force`.

------------------------------------------------------------------------

## Why Bash?

This tool focuses on **filesystem + workflow glue**, which is simple, transparent, and robust in Bash.
Python is excellent for parsing, logic, and building larger tools --- but for quick, direct system operations, Bash keeps it fast and
predictable.
