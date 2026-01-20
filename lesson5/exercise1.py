from rich import print
import re

filename = 'show_version.txt'

with open(filename) as f:
    data = f.read()

match = re.search(r'^cisco ([\w-]*) .*of memory\.$', data, flags=re.M)
if match:
    model = (match.group(1))

match = re.search(r'ID ([\w]+)$', data, flags=re.M)
if match:
    serial = (match.group(1))

print(f"{model=}")
print(f"{serial=}")