import random

rock_ui = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_ui = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_ui = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = ["rock", "paper", "scissors"]
yourChoice = input("Choose rock, paper or scissors: ")
computerChoice = choices[random.randint(0, 2)]
if yourChoice == choices[0]:
    print("Your choice: ")
    print(rock_ui)
    if computerChoice == choices[0]:
        print("Computer's choice: ")
        print(rock_ui)
        print("It's a tie.")
    elif computerChoice == choices[1]:
        print("Computer's choice: ")
        print(paper_ui)
        print("You lose.")
    elif computerChoice == choices[2]:
        print("Computer's choice: ")
        print(scissors_ui)
        print("You win.")
elif yourChoice == choices[1]:
    print("Your choice: ")
    print(paper_ui)
    if computerChoice == choices[0]:
        print("Computer's choice: ")
        print(rock_ui)
        print("You win.")
    elif computerChoice == choices[1]:
        print("Computer's choice: ")
        print(paper_ui)
        print("It's a tie.")
    elif computerChoice == choices[2]:
        print("Computer's choice: ")
        print(scissors_ui)
        print("You lose.")
elif yourChoice == choices[2]:
    print("Your choice: ")
    print(scissors_ui)
    if computerChoice == choices[0]:
        print("Computer's choice: ")
        print(rock_ui)
        print("You lose.")
    elif computerChoice == choices[1]:
        print("Computer's choice: ")
        print(paper_ui)
        print("You win.")
    elif computerChoice == choices[2]:
        print("Computer's choice: ")
        print(scissors_ui)
        print("It's a tie.")
else:
    print("Your choice is invalid.")
