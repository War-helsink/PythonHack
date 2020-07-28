#/usr/bin/env python3.7
import subprocess
from re import search


class Macchanger:
    def __init__(self, interface, new_mac):
        self.interface = interface
        self.new_mac = new_mac

    def changed_mac(self):
        a = self.current_mac()
        print("[+] Your current MAC address " + str(a))
        print("[+] Changing MAC address for " + self.interface + " to " + self.new_mac)
        subprocess.call(["ifconfig", self.interface, "down"])
        subprocess.call(["ifconfig", self.interface, "hw", "ether", self.new_mac])
        subprocess.call(["ifconfig", self.interface, "up"])
        a = self.current_mac()

    def current_mac(self):
        a = subprocess.check_output(["ifconfig", self.interface])
        a = search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(a))
        if a:
            return a.group(0)
        else:
            print("[-] Could not read MAC address.")

    def if_address(self):
        a = str(self.current_mac())
        if self.new_mac == a:
            print("[+] MAC address was successfully changed " + self.new_mac)
        else:
            print("[-] MAC address did not get changed.")

    def run(self):
        self.changed_mac()
        self.if_address()
