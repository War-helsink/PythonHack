#!/usr/bin/env python

import scapy.all as scapy


def ARP_scan(ip):
    scapy.arping(ip)


ARP_scan("192.168.0.1/24")


