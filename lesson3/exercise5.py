# with open("junos_show_arp.txt") as f:
#     ip_addresses = []
#     mac_addresses = []
#     fields = []
#     lines = f.readlines()[1:4]
#     for line in range(len(lines)):
#         fields.append(lines[line].split())
#     for idx in range(len(lines)):
#         ip_addresses.append(fields[idx][1])
#         mac_addresses.append(fields[idx][0].replace(':','-'))

    
# print(ip_addresses)
# print(mac_addresses)


from rich import print

filename = 'junos_show_arp.txt'

print()
print('Junos ARP Table')
print('-' * 50)

with open(filename) as f:
    for line in f:
        if 'MAC' in line or 'Total' in line:
            continue
        mac_addr, ip_addr, *rest = line.split()
        alt_mac_addr = mac_addr.replace(':', '-')
        print(f'{ip_addr:14} --> {alt_mac_addr}')

print('-' * 50)
print()