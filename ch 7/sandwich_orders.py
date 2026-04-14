sandwich_orders = ['blt','meatball sub','cajun chicken']
complete_orders = []

while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"Making your {current} sandwich.")
    complete_orders.append(current)

print("I have made the following sandwiches:")
for complete_order in complete_orders:
    print(complete_order.title())