#!/usr/bin/env python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(5)
client, addr = s.accept()
print("[+] New connect.")
while True:
    try:
        command = input("[+]Connect>>")
        bite = command.encode('utf-8')
        client.send(bite)
        result = client.recv(2048)
        print(result.decode('utf-8'))
    except Exception:
        break

s.close()