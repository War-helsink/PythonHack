#!/usr/bin/env python
import socket, subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))
g = subprocess.check_output(["ifconfig", "wlan0"])
s.send(g)
s.close()
