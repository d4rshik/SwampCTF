# SwampCTF
# Orcish writeup for SwampCTF 2018

Hello Everyone!

So I found this challenge a bit tiring. We get a lot of data sent through different protocols (ARP, MDNS, TCP, ICMP etc.)
Going through all of them, I found the ICMP packets a bit strange. There were some malformed packets in the capture.
Seeing the hexdump of the first 3 packets makes it clear that a GIF image's characters are present at the 34th byte of the hexdump.

So we got the exploit. All that is needed now is to filter out the ICMP packets which have the source IP 10.136.255.127.

Then run a simple scapy script thats all. My script is available as ex.py in this repo.

Cheers!!
