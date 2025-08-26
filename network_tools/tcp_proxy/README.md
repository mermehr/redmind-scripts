# TCP Proxy Tool

This script (`proxy.py`) is a simple TCP proxy designed for inspecting,
relaying, and optionally modifying traffic between a local client and a
remote host. It's useful for debugging, learning protocol structures,
and performing man-in-the-middle style analysis in controlled
environments.

------------------------------------------------------------------------

## Features

-   **Hexdump output**: Shows raw packet contents in hex and ASCII for
    inspection.
-   **Request and response handlers**: Functions (`request_handler` and
    `response_handler`) allow you to modify traffic before it is
    forwarded.
-   **Bidirectional proxying**: Relays data between a local client and a
    remote server.
-   **Threaded handling**: Each client connection spawns a new thread
    for concurrent proxying.
-   **Configurable receive-first option**: Useful for protocols where
    the server speaks first.

------------------------------------------------------------------------

## Usage

``` bash
python3 proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]
```

### Example

``` bash
python3 proxy.py 127.0.0.1 9000 example.com 80 True
```

-   `localhost`: Local interface to listen on (e.g., `127.0.0.1`)
-   `localport`: Local port to bind (e.g., `9000`)
-   `remotehost`: Remote host to connect to (e.g., `example.com`)
-   `remoteport`: Remote port to connect to (e.g., `80`)
-   `receive_first`: `True` if the remote server sends data immediately
    upon connection (common with some banners or protocol greetings),
    else `False`.

------------------------------------------------------------------------

## Extending Functionality

-   **Request Modification**\
    Edit the `request_handler(buffer)` function to inspect or alter data
    before sending it to the remote host.

-   **Response Modification**\
    Edit the `response_handler(buffer)` function to manipulate responses
    before sending them back to the local client.

-   **Hexdump Utility**\
    The `hexdump()` function can be used independently for debugging
    payloads.

------------------------------------------------------------------------

## Notes

-   The default buffer size for receiving data is **4096 bytes**. Adjust
    if necessary for large payloads.
-   Connections automatically close when no more data is available from
    either side.
-   Requires Python 3.x.
-   Intended for controlled lab environments (CTF, protocol analysis,
    testing). **Do not use this against systems without authorisation.**

------------------------------------------------------------------------

## Future Enhancements

-   Add logging to file for captured traffic.
-   Implement command-line switches for buffer size and verbosity.
-   Support UDP sockets in addition to TCP.
