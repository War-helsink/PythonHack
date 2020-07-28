import random
def version():
    a = ["""
\033[34m|_ Version:0.1.2.1
|_ Aytor: War-helsink.
|_ Sniffer. !!!
|_ Sniffer ARP, local network. !!!
|_ Sniffer ICMP, External network. !!!
|_ Sniffer port TCP. !!!\033[0m
    """,
             """
\033[31m|_ Version:0.1.2.1
|_ Aytor: War-helsink.
|_ Sniffer. !!!
|_ Sniffer ARP, local network. !!!
|_ Sniffer ICMP, External network. !!!
|_ Sniffer port TCP. !!!\033[0m
             """
            , """
\033[33m|_ Version:0.1.2.1
|_ Aytor: War-helsink.
|_ Sniffer. !!!
|_ Sniffer ARP, local network. !!!
|_ Sniffer ICMP, External network. !!!
|_ Sniffer port TCP. !!!\033[0m
             """
            , """
\033[32m|_ Version:0.1.2.1
|_ Aytor: War-helsink.
|_ Sniffer. !!!
|_ Sniffer ARP, local network. !!!
|_ Sniffer ICMP, External network. !!!
|_ Sniffer port TCP. !!!
\033[0m
    """]
    return a[random.randint(0, 3)]