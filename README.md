# SwampCTF
# Orcish writeup for SwampCTF 2018

## Hello Everyone!

So I found this challenge a bit tiring. We get a lot of data sent through different protocols (ARP, MDNS, TCP, ICMP etc.)
Going through all of them, I found the ICMP packets a bit strange. There were some malformed packets in the capture.
Seeing the hexdump of the first 3 packets makes it clear that a GIF image's characters are present at the 34th byte of the hexdump.

So we got the exploit. All that is needed now is to filter out the ICMP packets which have the source IP 10.136.255.127.

## The suspicious ICMP packets:

![alt text](https://github.com/stuxnet999/SwampCTF/blob/master/Screenshot%20from%202018-05-11%2017-10-17.png "ICMP 1")
The highlighted byte in the picture **G**

![alt text](https://github.com/stuxnet999/SwampCTF/blob/master/Screenshot%20from%202018-05-11%2017-10-27.png "ICMP 2")
The highlighted byte in the picture **I**

![alt text](https://github.com/stuxnet999/SwampCTF/blob/master/Screenshot%20from%202018-05-11%2017-10-41.png "ICMP 1")
The highlighted byte in the picture **F**

After analyzing the first 5 packets and combining the data at the 34th byte gives me **GIF89**

Then run a simple scapy script thats all.
Just to make you confident, please analyze every line of code and then run the complete script.

```python
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
```

Then we get a .GIF file with the flag written.

![alt text](https://github.com/stuxnet999/SwampCTF/blob/master/FLAG.gif "flag.gif")

Well that was some challenge!

Cheers!!
