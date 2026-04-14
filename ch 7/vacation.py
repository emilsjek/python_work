vacation = {}

active = True

while active:
    name = input("What is your name?: ")
    response = input("\nWhere is your dream vacation?: ")

    vacation[name] = response

    repeat = input("\nIs anyone else going to answer? (n/y): ")

    if repeat == 'n':
        active = False

print("\nHere is everyone's dream vacation: ")
for name, response in vacation.items():
    print(f"{name.title()} would like to go to {response.title()}")