#!/usr/bin/env python
import requests


def download(url):
    get_request = requests.get(url)


download(r"https://s00.yaplakal.com/pics/pics_original/3/0/3/13224303.jpg")