import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 5678))
s.listen()
conn, addr = s.accept()

print("Connection:", conn, addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(b"Echo"+data)

print("baba")
s.close()
