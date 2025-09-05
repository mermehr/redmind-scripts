# Repo Sync Script

A simple Bash utility to automatically sync a local Git repository with its remote counterpart.  
This script is designed to run cleanly from cron jobs or manual execution without requiring interactive input.

---

## Features

- `set -euo pipefail` for safe execution
- Pulls the latest changes from the remote
- Adds and commits local changes
- Pushes updates back to the remote
- Works with SSH key authentication and GTK keyring via **keychain**

---

## Installation & Requirements

- **Dependencies**
  - Git (installed and available in your `$PATH`)
  - Bash (tested on Linux Mint / Ubuntu)
  - Optional: [`keychain`](https://www.funtoo.org/Keychain) to persist your SSH agent across logins and cron
  - Optional: GNOME Keyring (**gtk** keyring) / Seahorse for securely storing keys

- **Make the script executable**
  ```bash
  chmod +x repo-sync.sh
  ```

---

## SSH Setup for GitHub (ed25519)

1. **Generate a new key (recommended: ed25519)**  
   ```bash
   mkdir -p ~/.ssh && chmod 700 ~/.ssh
   ssh-keygen -t ed25519 -C "your_email@example.com"
   # Save to: ~/.ssh/id_ed25519   (press Enter to accept default)
   # Choose a passphrase when prompted (recommended)
   chmod 600 ~/.ssh/id_ed25519
   chmod 644 ~/.ssh/id_ed25519.pub
   ```

2. **Start an SSH agent and add your key (one‑time to test)**  
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```

3. **Add the public key to GitHub**  
   
   - Copy the key:  
   
   ```bash
   xclip -selection clipboard < ~/.ssh/id_ed25519.pub  # or: cat ~/.ssh/id_ed25519.pub
   ```
   
   - GitHub → **Settings** → **SSH and GPG keys** → **New SSH key** → paste your public key.
   
4. **Switch your repo remote to SSH**  
   
   ```bash
   git remote -v  # inspect current remotes
   git remote set-url origin git@github.com:<USER>/<REPO>.git
   ```
   
5. **Test connectivity**  
   ```bash
   ssh -T git@github.com
   # Expected once: "Hi <username>! You've successfully authenticated…"
   ```

---

## Using `keychain` + GTK Keyring (GNOME Keyring)

`keychain` is a shell helper that manages a single long‑lived `ssh-agent` session and makes it available to your shells *and* cron jobs. 

GNOME Keyring (GTK keyring) can securely store your passphrase so you’re not prompted repeatedly.

### Install

```bash
# Debian/Ubuntu/Mint
sudo apt update
sudo apt install keychain gnome-keyring seahorse
```

### Configure keychain at login

Add the following to your shell init (choose one that your login session uses, e.g. `~/.bash_profile`, `~/.profile`, or `~/.bashrc`).  

This will start (or reuse) a single `ssh-agent`, load your key, and write helper files under `~/.keychain/`.

```bash
# --- keychain setup ---
if command -v keychain >/dev/null 2>&1; then
  eval "$(keychain --quiet --agents ssh --eval ~/.ssh/id_ed25519)"
fi
# --- end keychain setup ---
```

Log out and back in (or source the file):  
```bash
source ~/.bashrc   # or ~/.profile
```

You should see `~/.keychain/<hostname>-sh` created. That file exports `SSH_AUTH_SOCK` and `SSH_AGENT_PID` for re-use.

### Make cron jobs inherit the agent

Edit your crontab with `crontab -e` and **source the keychain export** at the top of the crontab or inside each job command:

**Option A – crontab header (recommended):**
```cron
# Load keychain environment for all cron jobs
SHELL=/bin/bash
BASH_ENV=~/.keychain/$(hostname)-sh
```

**Option B – per‑job sourcing:**
```cron
30 3 * * * . ~/.keychain/$(hostname)-sh; /path/to/repo-sync.sh >> /path/to/repo-sync.log 2>&1
```

> If you previously saw errors like `mkdir: cannot create directory '/.keychain': Permission denied`, ensure you did **not** prefix home with `/` accidentally. The correct directory is `~/.keychain` inside your home.

### Store passphrase in GTK keyring (optional but convenient)

1. Launch **Seahorse** (Passwords and Keys) → **File → New** → **Secure Shell Key** → Import `~/.ssh/id_ed25519` or create/manage keys there.  
2. Ensure **“Automatically unlock keyring when I log in”** is enabled (Mint: *Startup Applications* → **GNOME Keyring** helpers enabled).  
3. On your next login, your SSH key will be unlocked by GTK keyring, and `keychain` will pick it up without prompting.

---

## Usage

Run the script from **inside a Git repository**:

```bash
./repo-sync.sh
```

Typical flow (simplified):
1. Verify Git repo state
2. `git pull --rebase` (or merge, depending on your script’s flags)
3. Stage changes, create a message, and commit if needed
4. `git push` to remote

---

## Automating with Cron (example)

Daily sync at **03:30** with a shared keychain agent:

```cron
SHELL=/bin/bash
BASH_ENV=~/.keychain/$(hostname)-sh
30 3 * * * /path/to/repo-sync.sh >> /path/to/repo-sync.log 2>&1
```

---

## Troubleshooting

- **Permissions**  
  ```bash
  chmod 700 ~/.ssh
  chmod 600 ~/.ssh/id_ed25519
  chmod 644 ~/.ssh/id_ed25519.pub
  ```

- **Agent not available in cron**  
  Ensure your crontab sources `~/.keychain/$(hostname)-sh` (see above).

- **Wrong remote URL**  
  `git remote -v` should show `git@github.com:USER/REPO.git` (SSH), not HTTPS.

- **Host key verification failure**  
  First connect interactively: `ssh -T git@github.com` so `~/.ssh/known_hosts` is populated.

- **Multiple desktops / TTYs**  
  Use **keychain** to avoid spawning multiple `ssh-agent` instances; re-use the same one across sessions.

---

## Example Commit Messages (auto-sync)

If your script auto-commits, consider a standard message format:

```
chore(sync): auto-sync $(date -Iseconds)
```

This keeps the history clean and searchable.

---

