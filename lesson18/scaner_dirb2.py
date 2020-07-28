#!/usr/bin/env python
# Все домены из файла
import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "google.com"

with open("/root/subdomains.list", "r") as word_list_file:
    for line in word_list_file:
        test_url = line+"."+target_url
        response = requests(test_url)
        if response:
            print("[+] Discovered subdomain --> "+test_url)