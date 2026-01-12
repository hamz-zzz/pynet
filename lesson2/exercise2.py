f = open('show_version.txt')
data = f.read()

print('*'*80)
print(f"First line: {data.splitlines()[0]}")
print('*'*80)
print(f"Type: {type(data)}")
print('*'*80)

f.close()

print('')

with open('show_version.txt') as f:
    data = f.readlines()

print('*'*80)
print(f"First line: {data[0].strip()}")
print('*'*80)
print(f"Type: {type(data)}")
print('*'*80)