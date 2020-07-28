#!/usr/bin/env python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(1)
while True:
    try:
        client, addr = s.accept()
        r = client.recv(2048)
        client.close()
        print(r.decode('utf-8'))
    except Exception:
        s.close()
        break
s.close()