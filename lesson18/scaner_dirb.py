#!/usr/bin/env python
import requests


url = "google.com"
get_response = requests.get("http://" + url)
print(get_response)