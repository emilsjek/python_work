print("---The Menu---")
menu = ('burger', 'chips',  'pizza', 'icecream')
for food in menu:
    print(food.title())

#checking append can be used on lists but not on tuple
print("\n---The new menu---")
menu = ["cherry's", 'coke', 'pizza', 'icecream']
for food in menu:
    print(food.title())

print("\n---The Newest Menu---")
menu.append('pineapple')
for food in menu:
    print(food.title())