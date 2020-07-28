#!/usr/bin/env python


import subprocess, optparse
from re import search


def get_agent():
    p = optparse.OptionParser()
    p.add_option("-i", "--interface", dest="interface", help="Interface to change")
    p.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = p.parse_args()
    if not options.interface:
        p.error("[-] Please specify an interface, use --help for more into.")
    elif not options.new_mac:
        p.error("[-] Please specify an New MAC address, use --help for more into.")
    return options


def change_mac(interface, new_mac):
    a = current_mac(interface)
    print("[+] Your current MAC address " + str(a))
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    a = current_mac(interface)
    print("[+] Your new MAC address " + str(a))


def current_mac(interface):
    a = subprocess.check_output(["ifconfig", interface])
    a = search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(a))
    if a:
        return a.group(0)
    else:
        print("[-] Could not read MAC address.")


options = get_agent()
change_mac(options.interface, options.new_mac)