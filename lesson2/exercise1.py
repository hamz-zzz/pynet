base = '192.168.254.'

prefix_length = int(input('Enter a prefix length between 25 to 30: '))

subnet_size = 2**(32 - prefix_length)

hosts = subnet_size - 2
print(f"Number of hosts: {hosts}")

network1 = f"{base}0"
network2 = f"{base}{subnet_size}"
print(f"Network 1: {network1}")
print(f"Network 2: {network2}")

first = f"{base}1"
last = f"{base}{hosts}"
print(f"First address: {first}")
print(f"Last address: {last}")