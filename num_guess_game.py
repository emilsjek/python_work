import random

num = random.randint(1,100)

while True:
    guess = input("Guess the number from 1 to 100: ")
    guess = int(guess)
    if guess == num:
        print("That's correct! You win!")
        break
    elif guess >= num:
        print('Lower!')
    elif guess <= num:
        print('Higher!')
    else:
        print('Invalid Input')

