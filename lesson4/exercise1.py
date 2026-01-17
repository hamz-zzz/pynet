from rich import print

# lines = []
# ip = {}

# with open("show_ip_int_brief.txt") as f:
#     for line in f:
#         if '10' in line:
#             lines.append(line)

# for idx in range(len(lines)):
#     ip[lines[idx].split()[0]] = lines[idx].split()[1]


# print(ip)


filename = 'show_ip_int_brief.txt'

with open(filename) as f:
    data = f.read()

interface_ips = {}


for line in data.splitlines():
    intf, ip_addr, *other = line.split()

    if ip_addr in ['unassigned', 'IP-Address']:
        continue

    interface_ips[intf] = ip_addr

print(interface_ips)