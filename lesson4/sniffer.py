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
            print(packet[scapy.Raw].load)


a = argument()
sniffer(a.interface)