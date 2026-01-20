from rich import print
import re

filename = 'aruba_cx_show_ipv6_intf.txt'

with open(filename) as f:
    data = f.read()

m = re.search(r'^\S+ ([\d\/]+) is (\w+)', data, flags=re.M)
if m:
    intf_name = m.group(1)
    intf_state = m.group(2)

m = re.search(r'^A.* (\w+)$', data, flags=re.M)
if m:
    admin_state = m.group(1)

m = re.search(r'^\s+([\w:\/]+)', data, flags=re.M)
if m:
    ipv6_addr = m.group(1)

print(f"{intf_name=}")
print(f"{intf_state=}")
print(f"{admin_state=}")
print(f"{ipv6_addr=}")