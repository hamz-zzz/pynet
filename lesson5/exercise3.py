from rich import print
import re

filename = 'arista_show_ip_arp.txt'

with open(filename) as f:
    data = f.read()

ip_addr = r'[\d\.]+'
mac_addr = r'\w+\.\w+\.\w+'

pattern = rf'^({ip_addr})\s+\S+\s+({mac_addr})\s+'

match = re.findall(pattern, data, flags=re.M)
# match = re.findall(r'^([\d\.]+)\s+\S+\s+(\w+\.\w+\.\w+)\s+', data, flags=re.M)

if match:
    arp = dict(match)
    print(arp)