#!/usr/bin/env python
import scapy.all as scapy


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniff)


def process_sniff(packet):
        if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
            print(packet.show())


sniff("wlan0")