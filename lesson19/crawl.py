#!/usr/bin/env python
# Извлекаю силки с сайта
import requests
import re
import urllib.parse as urlparse


target_url = "http://192.168.56.7/mutillidae/"
target_link = []


def extract_link_from(url):
    try:
        response = requests.get(url)
        return re.findall(r'(?:href=")(.*?)"', response.content.decode('utf-8'))
    except UnicodeDecodeError:
        return ""


def crawl(url):
    href_links = extract_link_from(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]
        if target_url in link and link not in target_link:
            target_link.append(link)
            print(link)
            crawl(link)


crawl(target_url)