from rich import print
import re

filename = 'show_ip_bgp_neighbors.txt'

with open(filename) as f:
    data = f.read()


match = re.search(r'neighbor is (?P<bgp_neighbor_ip>[\d.]+),.*AS (?P<remote_as>\d+),.*version (?P<bgp_version>\d+),.*router ID (?P<remote_router_id>[\d.]+).*state = (?P<bgp_state>\w+),.*?$', data, flags=re.DOTALL | re.M)
if match:
    bgp_neighbor_ip = match.group('bgp_neighbor_ip')
    remote_as = match.group('remote_as')
    bgp_version = match.group('bgp_version')
    remote_router_id = match.group('remote_router_id')
    bgp_state = match.group('bgp_state')

print(f"{bgp_neighbor_ip=}")
print(f"{remote_as=}")
print(f"{bgp_version=}")
print(f"{remote_router_id=}")
print(f"{bgp_state=}")