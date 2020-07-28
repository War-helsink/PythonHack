#!/usr/bin/env python
import netfilterqueue
import subprocess
import optparse
import scapy.all as scapy


def process_packet(packet):
    ip_packet = scapy.IP(packet.get_payload())
    if ip_packet.haslayer(scapy.DNSRR):
        print(ip_packet.show())
    packet.accept()


try:
    subprocess.call("iptables -I UOTPUT -j NFQUEUE --gueue-num 0")
    queue = netfilterqueue.NerfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
except Exception:
    subprocess.call("iptables -F")
    print("[-] Detected CTRL + C ...... \n[+] Quitting .....")