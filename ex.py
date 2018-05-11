from scapy.all import *

r = rdpcap("data.pcap")

list1 = []

for i in range(0, len(r)):
    if ICMP in r[i]:
        if "ICMP 10.136.255.127" in r[i][ICMP].summary(): #getting the correct packets by filtering w.r.t source IP
        	d = str(r[i])
        	list1.append(d[34]) # 34th byte in every packet has GIF file code
f = open('FLAG.gif', 'w')
f.write(''.join(list1))
f.close()