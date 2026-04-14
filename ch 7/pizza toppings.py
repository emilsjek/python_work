toppings = "If you have selected all your topics type 'stop'."
toppings += "\nAdd any topic you would like:"
pizza = []

active = True
while active:
    selection = input(toppings)
    if selection == 'stop':
        active = False
    else:
        pizza.append(selection)
        print(f"Your toppings are: {pizza}.")