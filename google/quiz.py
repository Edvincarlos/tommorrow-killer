import random

secret_number = random.randint(1,100)
player_guess = int(input("what's your guess "))
guess = 0
while guess != secret_number:
    if player_guess == secret_number:
        print("you got it")
        break
    elif player_guess > secret_number:
        print("Too high!")
    elif player_guess < secret_number:
        print("Too low!")
    else:
        print("invalid input")