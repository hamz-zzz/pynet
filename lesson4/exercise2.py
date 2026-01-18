from rich import print

filename = 'show_ip_int_brief.txt'

with open(filename) as f:
    data = f.read()

outer_dict = {}
inner_dict = {}


for line in data.splitlines():
    intf, ip_addr, _, _, *fields = line.split()

    if intf == 'Interface':
        continue

    if len(fields) == 2:
        line_status = fields[0]
        line_protocol = fields[1]

    elif len(fields) == 3:
        line_status = "_".join(fields[:2])
        line_protocol = fields[2]
    
    else:
        msg = "Unexpected Error"
        raise ValueError(msg)

    outer_dict[intf] = {
        'ip_addr': ip_addr,
        'line_status': line_status,
        'line_protocol': line_protocol
    }

print(outer_dict)