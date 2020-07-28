#!/usr/bin/env python
# Извлекаю силки с сайта и силки с силок 
import requests
import re
import urllib.parse as urlparse


target_url = "https://zsecurity.org"
target_link = []


def extract_link_from(url):
    response = requests.get(target_url)
    return re.findall(r'(?:href=")(.*?)"', response.content.decode('utf-8'))


href_links = extract_link_from(target_url)
for link in href_links:
    link = urlparse.urljoin(target_url, link)
    if "#" in link:
        link = link.split("#")[0]

    if target_url in link and link not in target_link:
        target_link.append(link)
        print(link)
