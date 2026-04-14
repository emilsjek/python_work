guests = input("How many guests will be joining you today?: ")

guests = int(guests)

if guests > 8:
    print("You will have to wait for a table.")
if guests <= 8:
    print("A table is ready for you")
    