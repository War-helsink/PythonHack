#!/usr/bin/env python
import requests, re


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "zsecurity.org"
response = request(target_url)
href_links = re.findall(r'(?:href=")(.*?)"', response.content.decode('utf-8'))
print(href_links)
