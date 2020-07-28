#!/usr/bin/env python

import subprocess
import re
subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
b = subprocess.check_output(["ifconfig", "wlan0"])
b = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(b))
try:
    print(b.group(0))
except:
    print("[-] Could not read MAC address.")