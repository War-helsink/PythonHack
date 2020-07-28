#!/usr/bin/env python
# Все домены из файла
import requests
from bs4 import BeautifulSoup
from urllib import parse


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "http://192.168.56.7/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)
parsed_html = BeautifulSoup(response.content, features="lxml")
html_code = parsed_html.find_all("form")
for fond in html_code:
    action = fond.get("action")
    url_parse = parse.urljoin(target_url, action)
    method = fond.get("method")
    input_form = fond.find_all("input")
    post_data = {}
    for inputs in input_form:
        name_input = inputs.get("name")
        type_input = inputs.get("type")
        value_input = inputs.get("value")
        if type_input == "text":
            value_input = "test"
        post_data[name_input] = value_input
    result = requests.post(url_parse, data=post_data)
    print(result.content.decode('utf-8'))