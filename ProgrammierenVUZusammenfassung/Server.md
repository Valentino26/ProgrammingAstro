Now that you’ve gotten an overview of the socket API and how the client and server communicate, you’re ready to create your first client and server. You’ll begin with a simple implementation. The server will simply echo whatever it receives back to the client.

```python3
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

```

The values passed to `.bind()` depend on the [address family](https://realpython.com/python-sockets/#socket-address-families) of the socket. In this example, you’re using `socket.AF_INET` (IPv4). So it expects a two-tuple: `(host, port)`.

`host` can be a hostname, [IP address](https://realpython.com/python-ipaddress-module/), or empty string. If an IP address is used, `host` should be an IPv4-formatted address string. The IP address `127.0.0.1` is the standard IPv4 address for the [loopback](https://en.wikipedia.org/wiki/Localhost) interface, so only processes on the host will be able to connect to the server. If you pass an empty string, the server will accept connections on all available IPv4 interfaces.

`port` represents the [TCP port](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_ports) number to accept connections on from clients. It should be an integer from `1` to `65535`, as `0` is reserved. Some systems may require superuser privileges if the port number is less than `1024`.

Here’s a note on using hostnames with `.bind()`:

> “If you use a hostname in the host portion of IPv4/v6 socket address, the program may show a non-deterministic behavior, as Python uses the first address returned from the DNS resolution. The socket address will be resolved differently into an actual IPv4/v6 address, depending on the results from DNS resolution and/or the host configuration. For deterministic behavior use a numeric address in host portion.” [(Source)](https://docs.python.org/3/library/socket.html)

You’ll learn more about this later, in [Using Hostnames](https://realpython.com/python-sockets/#using-hostnames). For now, just understand that when using a hostname, you could see different results depending on what’s returned from the name resolution process. These results could be anything. The first time you run your application, you might get the address `10.1.2.3`. The next time, you get a different address, `192.168.0.1`. The third time, you could get `172.16.7.8`, and so on.

In the server example, `.listen()` enables a server to accept connections. It makes the server a “listening” socket:

```python
```
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    # ...
```
```
