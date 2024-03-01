from scapy import*
from scapy.layers.dns import DNSQR, DNSRR, DNS
from scapy.layers.inet import UDP, IP, Ether

dst_dns = {'dst': "8.8.8.8", 'port': 53}
dst_retu = {}



def filter_dns(packet):
    return (DNS in packet and packet[DNS].opcode==0 and packet[DNSQR].qtype==1)

def rafi():
    pass