#!/usr/bin/env python
import volnerability_scanner


data_dict = {'username': "smithy", 'password': "password", 'Login': 'Login'}
links_to_ignore = ["http://192.168.56.13/dvwa/logout.php"]
url = "http://192.168.56.13/dvwa/"
scanner = volnerability_scanner.Scanner(url, links_to_ignore)
scanner.session.post("http://192.168.56.13/dvwa/login.php", data=data_dict)
scanner.run_scanner()