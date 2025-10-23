locations = ['Thailand','Singapore','Canada','Australia','New Zealand']

print("Here's the original list:")
print(locations)

print("\nHere is the sorted list:")
print(sorted(locations))

print("\nHere's the list back in it's original order:")
print(locations)

print("\nHere's the list in reverse alphabetical order:")
print(sorted(locations, reverse=True))

print("\nHere's the list back in it's original order:")
print(locations)

print("\nHere's the original list reversed:")
locations.reverse()
print(locations)

print("\nHere's the original list:")
locations.reverse()
print(locations)

print("\nHere's the list sorted:")
locations.sort()
print(locations)

print("\nHere's the list in reverse alphabetical order:")
locations.sort(reverse=True)
print(locations)