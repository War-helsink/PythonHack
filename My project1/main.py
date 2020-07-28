import macchenger
import optparse


if __name__ == '__main__':
    def argument():
        p = optparse.OptionParser()
        p.add_option("-m", "--mac", dest="mac", help="MAC address = \"-m\" or \"--mac\"")
        p.add_option("-i", "--interface", dest="interface", help="Time out")
        (option, arguments) = p.parse_args()
        if not option.mac or not option.interface:
            print("Enter MAC new address: --> -m or --mac")
            print("Enter the interface on which to change: --> -i or --interface")
            p.error()
        else:
            return option
    
    options = argument()
    new_mac = macchenger.Macchanger(option.mac,option.interface)
    new_mac.run()