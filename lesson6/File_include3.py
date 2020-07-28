#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy


ack_list = []


def process_packet(packet):
    ip_packet = scapy.IP(packet.get_payload())
    if ip_packet.haslayer(scapy.Raw):
        if ip_packet[scapy.TCP].dport == 80:
            if ".exe" == ip_packet[scapy.Raw].load:
                print("[+] HTTP Request port 80, exe file.")
                ack_list.append(ip_packet[scapy.TCP].ack)
                print(ip_packet.show())
        elif ip_packet[scapy.TCP].sport == 80:
            if ip_packet[scapy.TCP].set in ack_list:
                ack_list.remove(ip_packet[scapy.TCP].set)
                print("[+] HTTP Response port 80")
                print(ip_packet.show())
    packet.accept()


queue = netfilterqueue.NerfilterQueue()
queue.bind(0, process_packet)
queue.run()