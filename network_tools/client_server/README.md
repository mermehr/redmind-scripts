# Python Socket Examples

Simple **TCP** and **UDP** socket scripts for learning and as a base to extend into more advanced network tools.

---

## Contents

- `tcp_client.py` — Minimal TCP client that connects to `127.0.0.1:1337`, sends an HTTP‑style request, and prints the response.
- `tcp_server.py` — Threaded TCP server that listens on `127.0.0.1:1337`, prints received data, and replies with `ACK`.
- `udp_client.py` — Minimal UDP client that sends `AAABBBCCC` to `127.0.0.1:1337` and waits for a response.

> **Note:** There is **no UDP server** included yet. See the **TODO** section for guidance on creating `udp_server.py`.

---

## Quick Start

### 1) Run the TCP server
```bash
python3 tcp_server.py
# [*] Listening on 127.0.0.1:1337
```

### 2) In another terminal, run the TCP client
```bash
python3 tcp_client.py
# prints the server's response (or any data sent back)
```

### 3) Test the UDP client (requires a UDP server)
```bash
python3 udp_client.py
# waits to receive a UDP reply from 127.0.0.1:1337
```

---

## Requirements

- Python 3.x
- Standard library only (`socket`, `threading`)

---

## How These Scripts Work

### `tcp_client.py`
1. Creates a TCP socket.
2. Connects to `127.0.0.1:1337`.
3. Sends an HTTP‑style request.
4. Receives up to 4096 bytes and prints the decoded text.
5. Closes the connection.

**Extend it:**
- Add CLI flags for host/port/message (`argparse`).
- Add an interactive loop (send/receive until `Ctrl+C`).
- Wrap in a class for reuse in bigger tools.
- Add TLS (`ssl.wrap_socket` or `ssl.create_default_context()`).

---

### `tcp_server.py`
1. Binds a TCP socket to `127.0.0.1:1337`.
2. Listens and accepts connections.
3. Spawns a thread per client.
4. Prints the received bytes and replies with `ACK`.

**Extend it:**
- CLI flags for bind IP/port and backlog size.
- Simple protocol or HTTP parsing and proper responses.
- File logging with timestamps and client addresses.
- Switch to `asyncio` for high concurrency.

---

### `udp_client.py`
1. Creates a UDP socket.
2. Sends `AAABBBCCC` to `127.0.0.1:1337`.
3. Waits to receive a UDP datagram (up to 4096 bytes).
4. Prints the decoded response.

**Extend it:**
- CLI flags for host/port/payload.
- Retries + timeouts (`socket.settimeout`) since UDP is unreliable.
- Encode structured payloads (JSON/CBOR) and validate responses.

---

## Usage Examples

Run the server, then the client:

```bash
# Terminal A
python3 tcp_server.py

# Terminal B
python3 tcp_client.py
```

If you change ports or IPs in code, keep both sides in sync.

---

## Safety & Scope

These are lab/learning samples. Don’t expose them to untrusted networks without:
- Input validation
- Authentication/authorisation
- TLS
- Logging/monitoring
- Resource limits

---

## TODO

- **Add `udp_server.py`**  
  Create a simple UDP echo server so `udp_client.py` has something to talk to. Minimal behaviour:

  - Bind to `127.0.0.1:1337` using `socket.SOCK_DGRAM`.
  - In a loop, `recvfrom()` a datagram and print it.
  - `sendto()` a response (e.g., echo the payload or `ACK`) back to the sender’s `(addr, port)`.

  This will allow end‑to‑end UDP testing identical to how the TCP pair is used.

---

## Reference

These scripts are adapted from exercises in  **Black Hat Python, 2nd Edition** by Justin Seitz & Tim Arnold.  

They have been recreated here for personal study and educational purposes. The original book provides the full context, explanations, and ethical guidance for using these examples responsibly in security research.

**Important:** These scripts are for *learning and testing only* in controlled environments.  
Do not use them against systems you do not own or have explicit permission to test.

---

