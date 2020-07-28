import sniffer

if __name__ == '__main__':
    def argument():
        p = optparse.OptionParser()
        p.add_option("-m", "--mac", dest="mac", help="MAC address = \"-m\" or \"--mac\"")
        p.add_option("-i", "--interface", dest="interface", help="Time out")
        (option, arguments) = p.parse_args()
        if not option.interface:
            print("Enter the interface from which to sniff: --> -i or --interface")
            p.error()
        else:
            return option
    

    options = argument()
    a = sniffer.My_sniffer(options.interface)
    a.run()