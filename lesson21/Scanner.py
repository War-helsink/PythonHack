#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "http://192.168.56.7/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)
parsed_html = BeautifulSoup(response.content, features="lxml")
html_code = parsed_html.find_all("form")
print(html_code)