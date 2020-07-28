#/usr/bin/env python3.7
import random


def prints():
    return """
\033[1;3{}m|_ Version:0.1.2.1
|_ Aytor: War-helsink.
|_ Wlan scanner Network. !!!
|_ Scanner ARP, local network. !!!
|_ Scanner ICMP, External network. !!!
|_ Scanner port TCP. !!!
|_ ARP spoofing. !!!\033[0m
""".format(random.randint(1,5))