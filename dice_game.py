import random

while True:
    begin = input('Roll the dice? (y/n): ').lower()
    if begin == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(die1, die2)
    elif begin == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Input valid option.')
