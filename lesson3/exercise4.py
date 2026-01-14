with open("show_ip_int_brief.txt") as f:
    ip_addresses = []
    interface_names = []
    for line in f.readlines():
        if "10." in line:
            line = line.strip()
            intf_name, ip_addr, *fields = line.split()
            interface_names.append(intf_name)
            ip_addresses.append(ip_addr)

print(f"Interfaces: {interface_names}")
print(f"IP Addresses: {ip_addresses}")