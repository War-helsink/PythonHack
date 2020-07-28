#!/usr/bin/env python

import scapy.all as scapy
import optparse


def argument():
    p = optparse.OptionParser()
    p.add_option("-i", "--ip", dest="ip", help="IP address = \"-i\" or \"--ip\" ")
    p.add_option("-t", "--timeout", dest="timeout", help="Timeout packets.")
    (options, argument) = p.parse_args()
    if not options.ip and not options.timeout:
        p.error
    else:
        return options


def ARP_scan(ip, time=1):
    arp_scaner = scapy.ARP(pdst=ip) # создания своего арп запроса
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = brodcast/arp_scaner
    answered = scapy.srp(arp_packet, timeout=int(time), verbose=False)[0]
    print("_________________________________________________________________________")
    print("IP\t\t|\tMAC address\t\t|\tVession IP\t|")
    print("-------------------------------------------------------------------------")
    for element in answered:
        print(element[1].psrc + "\t|\t" + element[1].hwsrc + "\t|\t" + str(element[1].ptype) + "\t\t|")
        print("-------------------------------------------------------------------------")


a = argument()
ARP_scan(a.ip, a.timeout)