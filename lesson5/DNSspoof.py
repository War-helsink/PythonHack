import netfilterqueue


def process_packet(packet):
    packet.accept()


queue = netfilterqueue.NerfilterQueue()
queue.bind(0, process_packet)
queue.run()