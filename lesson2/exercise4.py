from rich import print

with open('show_arp.txt') as f:
    show_arp = f.readlines()

print(f"Data type: {type(show_arp)}")

print(f"Length: {len(show_arp)}")

header = show_arp[0].strip()
print(f"Header:\n{header}\n")

print(f"First Line:\n{show_arp[1].strip()}\n")
print(f"Last Line:\n{show_arp[-1].strip()}\n")

fields = header.split()
print(f"Fields:\n{fields}\n")

print(f"\nData type of fields: {type(fields)}\n")

print(f"\nEntries in fields: {len(fields)}\n")

print(f"\nFirst field: {fields[0]}\n")
print(f"\nLast field: {fields[-1]}\n")

#Modifications
fields[4] = 'Hardware_Addr'
fields.remove('(min)')
fields.remove('Addr')
print(f"\nFields after modifications: {fields}\n")