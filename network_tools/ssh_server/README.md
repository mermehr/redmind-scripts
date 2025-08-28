# SSH Command & Control Scripts

This repository contains a set of Python scripts built using the **Paramiko** library to demonstrate client-server command execution over SSH. The scripts are designed to work together as a minimal proof-of-concept for remote command execution and server emulation.

---

## Scripts Overview

### 1. `ssh_cmd.py`
A simple SSH client that connects to a target server and executes a single command.

- Prompts the user for credentials and server details.  
- Executes a command (default: `id`).  
- Prints standard output and error streams from the remote host.

**Usage Example:**

```bash
python3 ssh_cmd.py
```

---

### 2. `ssh_rcmd.py`
A client-side script that establishes a reverse SSH session to a server.  
Once connected, it can receive and execute commands issued by the server.

- Connects to a remote SSH server with provided credentials.  
- Waits for server instructions and executes commands locally.  
- Sends command results back to the server.

**Usage Example:**
```bash
python3 ssh_rcmd.py
```

---

### 3. `ssh_server.py`
A custom SSH server that listens for incoming connections and provides an interactive command execution environment.

- Uses Paramiko’s `Transport` and `ServerInterface`.  
- Authenticates with hardcoded credentials (`tim:sekret`).  
- Supports interactive command execution until `exit` is issued.  
- Requires an RSA host key (`test_rsa.key`) in the same directory.

**Usage Example:**
```bash
python3 ssh_server.py
```

---

## Requirements

- Python 3.8+  
- [Paramiko](https://www.paramiko.org/)  

Install dependencies:
```bash
pip install paramiko
```

---

## Notes

- The scripts are for **educational purposes** only.  
- Authentication is currently hardcoded (in `ssh_server.py`) and should be updated for real deployments.  
- Ensure `test_rsa.key` exists in the same directory when running the server script. You can generate one with:

```bash
ssh-keygen -t rsa -b 2048 -f test_rsa.key
```

---

## Reference

These scripts are adapted from exercises in  **Black Hat Python, 2nd Edition** by Justin Seitz & Tim Arnold.  

They have been recreated here for personal study and educational purposes. The original book provides the full context, explanations, and ethical guidance for using these examples responsibly in security research.

**Important:** These scripts are for *learning and testing only* in controlled environments.  
Do not use them against systems you do not own or have explicit permission to test.

---

## Possible Extensions

- Improve authentication (e.g., public key or configurable credentials).  
- Add logging for connections and commands.  
- Wrap scripts into a more modular framework.  
