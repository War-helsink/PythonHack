#!/usr/bin/env python

import scapy.all as scapy
import optparse


def argument():
    p = optparse.OptionParser()
    p.add_option("-i", "--ip", dest="ip", help="IP address = \"-i\" or \"--ip\" ")
    p.add_option("-t", "--timeout", dest="timeout", help="Timeout packets.")
    (options, arguments) = p.parse_args()
    if not options.ip and not options.timeout:
        p.error
    else:
        return options


def ARP_scan(ip, time=1):
    arp_scaner = scapy.ARP(pdst=ip) # создания своего арп запроса
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = brodcast/arp_scaner
    answered = scapy.srp(arp_packet, timeout=int(time), verbose=False)[0]

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


if __name__ == '__main__':
    a = argument()
    print(r"""
   _____         __                 .___.__.__      _________                                  
  /  _  \_______|  | __ _____     __| _/|__|__|    /   _____/ ____ _____    ____   ___________ 
 /  /_\  \_  __ \  |/ / \__  \   / __ | |  |  |    \_____  \_/ ___\\__  \  /    \_/ __ \_  __ \
/    |    \  | \/    <   / __ \_/ /_/ | |  |  |    /        \  \___ / __ \|   |  \  ___/|  | \/
\____|__  /__|  |__|_ \ (____  /\____ | |__|__|   /_______  /\___  >____  /___|  /\___  >__|   
        \/           \/      \/      \/                   \/     \/     \/     \/     \/       """)
    print_result(ARP_scan(a.ip, a.timeout))