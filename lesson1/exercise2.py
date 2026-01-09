data_center = input("Enter data center location: ")

print("Upper case:")
print(data_center.upper())

print("Strip off whitespace:")
print(f"Before: {repr(data_center)}")
print(f"After: {repr(data_center.strip())}")

print("Method chaining:")
print(repr(data_center).strip().upper)