Cars = ['ferrari','ford', 'opel', 'vw', 'audi']
for car in Cars[:3]:
    print(car.title())

middle = len(Cars)//2
middle_three = Cars[middle-1:middle+2]
print(middle_three)

for car in Cars[-3:]:
    print(car.title())