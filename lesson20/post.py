#!/usr/bin/env python
import requests
url = "http://192.168.56.7/dvwa/login.php"
data_dict = {
    'username': "admin",
    'password': "password",
    'Login': 'Login'
    }
response = requests.post(url, data=data_dict)
print(response.content.decode('utf-8'))