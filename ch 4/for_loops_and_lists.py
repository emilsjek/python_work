
list = [number for number in range(1,1000001)]
print(min(list))
print(max(list))
print(sum(list))

odd_numbers = [numbers for numbers in range(1,21,2)]
print(odd_numbers)

multiples = []
for i in range (3,31,3):
    multiples.append(i)

print(multiples)

cubes = [value**3 for value in range(1,11)]
print(cubes)

