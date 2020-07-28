#!/usr/bin/env python
import scapy.all as scapy


def ARP_scan(ip, time=1):
    arp_scaner = scapy.ARP(pdst=ip) # создания своего арп запроса
    brodcasts = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packets = brodcasts/arp_scaner
    answered = scapy.srp(arp_packets, timeout=time, verbose=False)[0]
    return answered[0][1].hwsrc


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniff)


def process_sniff(packet):
        if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
            try:
                mac = ARP_scan(packet[scapy.ARP].psrc)
                if packet[scapy.ARP].hwsrc != mac:
                    print(r"""
       _____ ____________________      ____ ____    _____  _________  ____  __.
      /  _  \\______   \______   \    |    |    |  /  _  \ \_   ___ \|    |/ _|
     /  /_\  \|       _/|     ___/    |    ~    | /  /_\  \/    \  \/|      <  
    /    |    \    |   \|    |        |    Y    |/    |    \     \___|    |  \ 
    \____|__  /____|_  /|____|        |____|____|\____|__  /\______  /____|__ \
            \/       \/                                  \/        \/        \/ """)
            except ImportError:
                pass


sniff("wlan0")