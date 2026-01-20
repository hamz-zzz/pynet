from rich import print
import re

filename = 'show_lldp.txt'

with open(filename) as f:
    data = f.read()

pattern = r'Chassis.*?Vlan ID: not advertised'
lldp_entries = re.findall(pattern, data, flags=re.M | re.DOTALL)

pattern = r'Port id: (\w+\/\d).*Local Port id: (\w+\/\d).*System Name: (\w+\.\w+\.\w+)'

for entry in lldp_entries:
    # print(entry)
    match = re.search(pattern, entry, flags=re.DOTALL)
    if match:
        local_port = match.group(2)
        remote_system_name = match.group(3)
        remote_port = match.group(1)
        print('-'*37)
        print(f"{local_port=}")
        print(f"{remote_system_name=}")
        print(f"{remote_port=}")
        print('-'*37)
