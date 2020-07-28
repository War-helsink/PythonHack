#!/usr/bin/env python
import subprocess
import optparse
from re import search


def get_agent():
    p = optparse.OptionParser()
    p.add_option("-i", "--interface", dest="interface", help="Interface to change")
    p.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    # p.add_option("-r", "--random", dest="random", help="Random new MAC address")
    (options, arguments) = p.parse_args()
    if not options.interface:
        p.error("[-] Please specify an interface, use --help for more into.")
    elif not options.new_mac:
        p.error("[-] Please specify an New MAC address, use --help for more into.")
    return options


def changed_mac(interface, new_mac):
    a = current_mac(interface)
    print("[+] Your current MAC address " + str(a))
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    a = current_mac(interface)
    # print("[+] Your new MAC address " + str(a))


def current_mac(interface):
    a = subprocess.check_output(["ifconfig", interface])
    a = search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(a))
    if a:
        return a.group(0)
    else:
        print("[-] Could not read MAC address.")


def if_address(new_mac, interface):
    a = str(current_mac(interface))
    if new_mac == a:
        print("[+] MAC address was successfully changed " + new_mac)
    else:
        print("[-] MAC address did not get changed.")


options = get_agent()
changed_mac(options.interface, options.new_mac)
if_address(options.new_mac, options.interface)