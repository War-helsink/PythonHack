#!/usr/bin/env python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.100", 4444))
s.send(b"Hello my friend\n")
s.close()