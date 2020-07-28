#!/usr/bin/env python
# Извлекаю силки с сайта
import requests
import re
import urllib.parse as urlparse


def extract_link_from(url):
    response = requests.get(target_url)
    return re.findall(r'(?:href=")(.*?)"', response.content.decode('utf-8'))


target_url = "https://zsecurity.org"
href_links = extract_link_from(target_url)
for link in href_links:
    link = urlparse.urljoin(target_url, link)
    if target_url in link:
        print(link)
