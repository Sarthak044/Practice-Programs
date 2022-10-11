#!/usr/bin/python3

from time import process_time_ns
import netfilterqueue as nq
import scapy.all as scapy

''' 
To run this in your local system you have to run these commands
iptables -I INPUT -j NFQUEUE --queue-num 0
iptables -I OUTPUT -j NFQUEUE --queue-num 0

'''

ack_list = []

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] Request")
            print(scapy_packet.show())
            
        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] Response")
            print(scapy_packet.show())

            
    packet.accept()

queue = nq.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()
