def sandwiches(*toppings):
    print("\nMaking sandwich with these toppings: ")
    for topping in toppings:
        print(topping)

sandwiches('tomato','bacon','lettuce')
sandwiches('chicken','cajun')
sandwiches('ham')
