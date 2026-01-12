ip_addr = ['1.1.1.1', '8.8.8.8', '10.0.0.1', '192.168.1.1']
print(f"Initial list: {ip_addr}")

ip_addr.append('172.16.1.1')
print(f"a. {ip_addr}")

ip_addr.extend(['192.168.67.1', '153.24.45.252'])
print(f"b. {ip_addr}")

ip_addr += ['67.69.42.01', '127.0.0.1']
print(f"c. {ip_addr}")

print(f"d.\nEntire list: {ip_addr}\nFirst address: {ip_addr[0]}\nLast address: {ip_addr[-1]}")

ip_addr.pop(0)
ip_addr.pop()
print(f"e. {ip_addr}")

ip_addr[0] = '123.212.234.132'
print(f"f. {ip_addr[0]}")