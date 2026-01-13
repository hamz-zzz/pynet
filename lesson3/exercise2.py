with open('show_ip_int_brief.txt') as f:
    data = f.readlines()

for x in data:
    if '10.220' in x:
        lst = (x.split())

intf_name = lst[0]
ip_addr = lst[1]

print(f"Interface: {intf_name}")
print(f"IP Address: {ip_addr}")