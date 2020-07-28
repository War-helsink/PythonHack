#!/usr/bin/env python
# все файли на сервере из файла
import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "google.com"

with open("/root/subdomains.list", "r") as word_list_file:
    for line in word_list_file:
        word = word_list_file.sptrip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> "+test_url)