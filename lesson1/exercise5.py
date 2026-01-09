ip_addr = "10.12.17.1"
mac_addr = "0024.c4e9.48ae"

output = "String concatenation\n" + ip_addr + " --> " + mac_addr
print(output)

output= f"f-strings\nString concatenation\n{ip_addr} --> {mac_addr}"
print(output)

output = "format() method\nString concatenation\n{} --> {}".format(ip_addr, mac_addr)
print(output)