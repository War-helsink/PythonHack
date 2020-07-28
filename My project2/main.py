#/usr/bin/env python3.7
import scanner
import optparse

if __name__ == '__main__':
    def argument():
        p = optparse.OptionParser()
        p.add_option("-i", "--ip", dest="ip", help="IP address = \"-i\" or \"--ip\"")
        p.add_option("-t", "--time", dest="time", help="Time out")
        p.add_option("-s", "--arp-spoof", action="store_true", dest="arp_spoof", help="ARP spoofing True or False")
        p.add_option("-p", "--portscan", action="store_true", dest="portscan", help="False or True port scan")
        (option, arguments) = p.parse_args()
        if not option.ip:
            print("Enter the IP address to scan: --> -i or --ip")
            p.error()
        else:
            return option


    options = argument()
    if not options.time:
        options.time = 2
    if not options.portscan:
        options.portscan = False
    if not options.arp_spoof:
        options.arp_spoof = False

    a = scanner.Scanners_port(options.ip, options.time, options.portscan, options.arp_spoof)
    a.star()

