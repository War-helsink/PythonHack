#!/usr/bin/evn python
import requests
import re
import urllib.parse as urlparse
from bs4 import BeautifulSoup
from urllib import parse


class Scanner:
    def __init__(self, url, ignore_link):
        self.session = requests.Session()
        self.url = url
        self.links_to_ignore = ignore_link
        self.target_link = []

    def extract_link_from(self, url):
        try:
            response = self.session.get(url)
            return re.findall(r'(?:href=")(.*?)"', response.content.decode('utf-8'))
        except UnicodeDecodeError:
            return ""

    def crawl(self, url=None):
        if url == None:
            url = self.url
        href_links = self.extract_link_from(url)
        for link in href_links:
            link = urlparse.urljoin(url, link)
            if "#" in link:
                link = link.split("#")[0]
            if self.url in link and link not in self.target_link and link not in self.links_to_ignore:
                self.target_link.append(link)
                self.crawl(link)

    def extract_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content, features="lxml")
        return parsed_html.find_all("form")

    def submit_form(self, form, value, url):
        action = form.get("action")
        url_parse = parse.urljoin(url, action)
        method = form.get("method")
        input_form = form.find_all("input")
        post_data = {}
        for inputs in input_form:
            name_input = inputs.get("name")
            type_input = inputs.get("type")
            value_input = inputs.get("value")
            if type_input == "text":
                value_input = value
            post_data[name_input] = value_input
        if method == "post":
            return self.session.post(url_parse, data=post_data)
        return self.session.get(url_parse, params=post_data)

    def XSS_scannr_url(self, url):
        xss_text_test = "<sCriPt>alert(1);</sCriPt>"
        url = url.replace("=", "=" + xss_text_test)
        response = self.session.get(url)
        if xss_text_test in response.content.decode('utf-8'):
            return "[+][***] Get XSS yes-->" + url
        else:
            return None

    def XSS_scannr(self, form, url):
        xss_text_test = "<sCriPt>alert(1);</sCriPt>"
        result = self.submit_form(form, xss_text_test, url)
        if xss_text_test in result.content.decode('utf-8'):
            return "[+][***] POST XSS yes-->" + url
        else:
            return None

    def run_scanner(self):
        self.crawl()
        for link in self.target_link:
            forms = self.extract_forms(link)
            for form in forms:
                a = self.XSS_scannr(form, link)
                if a != None:
                    print(a)
            if "=" in link:
                b = self.XSS_scannr_url(link)
                if b != None:
                    print(b)


if __name__ == "__main__":
    print("Class Scanner")