customer = ("What age are you? :")

active = True

while active:
    age = input(customer)
    age = int(age)

    if age >= 0 and age < 3:
        price = 0
    elif age >= 3 and age <= 12:
        price = 10
    elif age > 12:
        price = 15 
    else:
        print("Invalid age.")
        active = False
        break
    print(f"Because you are {str(age)} years old, your ticket costs ${price}.")