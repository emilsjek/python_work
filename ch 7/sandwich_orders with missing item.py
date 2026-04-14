sandwich_orders = ['blt','pastrami','meatball sub','pastrami','cajun chicken','pastrami']

print("The Deli has ran out of pastrami.")

while 'pastrami' in sandwich_orders:
   sandwich_orders.remove('pastrami')

print("\nWe still have:")
for complete_order in sandwich_orders:
    print(complete_order.title())