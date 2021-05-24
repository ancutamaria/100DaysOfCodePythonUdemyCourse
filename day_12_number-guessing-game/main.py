import art
from random import randrange
print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
chosen_difficulty = input("Choose difficulty. Type 'easy' of 'hard': ")

computer_chosen_number = randrange(1, 100)

if chosen_difficulty == 'easy':
    attempts_left = 10
else:
    attempts_left = 5

while attempts_left > 0:
    print(f"You have {attempts_left} attempts remanining to guess the number.")
    chosen_number = int(input("Make a guess: "))
    if chosen_number == computer_chosen_number:
        print(f"You got it! The answer is {computer_chosen_number}")
        attempts_left = 0
    elif chosen_number > computer_chosen_number:
        print("Too high.")
        attempts_left -= 1
    else:
        print("Too low.")
        attempts_left -= 1

