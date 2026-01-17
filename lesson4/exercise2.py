from rich import print

filename = 'show_ip_int_brief.txt'

with open(filename) as f:
    data = f.read()

outer_dict = {}
inner_dict = {}


for line in data.splitlines():
    intf, ip_addr, *others, line_status, line_protocol = line.split()

    if intf == 'Interface':
        continue

    outer_dict[intf] = {
        'ip_addr': ip_addr,
        'line_status': line_status,
        'line_protocol': line_protocol
    }

print(outer_dict)