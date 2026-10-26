import random

num = random.randint(1,10)
guess = None

while guess != num:
    guess = int(input("guess a number between 1 and 10:"))
    guess = int(guess)
    if guess == num:
        print("you win!")
        break
    else:
        print("you lose")