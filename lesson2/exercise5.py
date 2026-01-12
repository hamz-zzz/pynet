from rich import print

intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"

intf_fields = intf.split()
print(intf_fields)

intf_name = intf_fields[0]
print(f"{intf_name=}")

intf_ip_addr = intf_fields[1]
print(f"{intf_ip_addr=}")

intf_status = intf_fields[-2]
print(f"{intf_status=}")

intf_protocol = intf_fields[-1]
print(f"{intf_protocol=}")


# intf_list = [intf_name, intf_ip_addr, intf_status, intf_protocol]

# for var in intf_list:
#     print(var)

status_is_up = intf_status == 'up'
protocol_is_up = intf_protocol == 'up'
print(f"{status_is_up=:}")
print(f"{protocol_is_up=}")