# Python Netcat Replacement

This script is a Python re‑implementation of **netcat (`nc`)**, useful on systems where netcat is not installed.  
It supports connecting to remote hosts, listening for incoming connections, executing commands, file uploads, and spawning an interactive shell.

---

## File

- `netcat.py` — Full TCP client/server utility with multiple features.

---

## Usage

The script uses command‑line arguments to mimic `nc` functionality.

Examples:

```bash
# Start a command shell on port 5555
python3 netcat.py -t 192.168.1.101 -p 5555 -l -c

# Upload a file to the server
python3 netcat.py -t 192.168.1.101 -p 5555 -l -u=mytest.txt

# Execute a command automatically when a client connects
python3 netcat.py -t 192.168.1.101 -p 5555 -l -e "cat /etc/passwd"

# Connect to a server and send text from stdin
echo 'ABC' | python3 netcat.py -t 192.168.1.101 -p 135

# Connect to a listening server interactively
python3 netcat.py -t 192.168.1.101 -p 5555
```

---

## Arguments

- `-t`, `--target` — Target IP (default: `192.168.1.203`)
- `-p`, `--port` — Target port (default: `5555`)
- `-l`, `--listen` — Listen mode (server mode)
- `-c`, `--command` — Start a command shell
- `-e`, `--execute` — Execute specified command
- `-u`, `--upload` — Upload file path to save received data

---

## Features

- **Client mode**: Connect to a host/port and interactively send/receive data.
- **Server mode**: Listen for incoming connections and handle:
  - Command execution
  - File uploads
  - Command shell sessions
- **Threaded handling**: Supports multiple connections in server mode.
- **Stdin piping**: Works with shell pipes for automation.

---

## Possible Expansions

- Add SSL/TLS support for encrypted sessions.
- Add IPv6 compatibility.
- Implement logging of sessions to a file.
- Extend to UDP support.
- Create a Python package wrapper for easy installation (`pip install`).

---

## Notes

- This script is for **educational and lab use only**.  
  Do not deploy on untrusted networks without proper security measures.
- Running it with `--listen` and `--command` effectively exposes a remote shell.  
  Use only in controlled environments.

---

