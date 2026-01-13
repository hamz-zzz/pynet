base_addr = '192.168.254.'

netmask = int(input('Enter a prefix length between 25 to 30: '))

subnet_size = 2 ** (32 - netmask)
print(f"Subnet Size: {subnet_size}")

hosts = subnet_size - 2
print(f"Number of hosts: {hosts}")

subnets = 2 ** (netmask - 24)
print(f"Number of subnets: {subnets}")

net = 0

for x in range(subnets):
    print(f"Subnet number: {base_addr}{subnet_size * x}")

first_addr = f'{base_addr}0'
last_addr = f'{base_addr}{hosts}'

print(f'First address of the first subnet: {first_addr}')
print(f'Last address of the first subnet: {last_addr}')