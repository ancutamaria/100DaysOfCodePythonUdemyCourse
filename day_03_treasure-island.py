print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("Near a lake, found an abandoned hut. Type left to walk past the hut or right to go inside it. ")
if choice.lower() == "left":
    choice = input("You arrived near the lake. Type wait or swim. ")
    if choice.lower() == "wait":
        choice = input("After a while, three doors appear. One blue, one red and one yellow. Type the color of the "
                       "door you want to enter. ")
        if choice.lower() == "red":
            print("There is a fire inside. You are burned.")
            print("Game over. ^_^")
        elif choice.lower() == "blue":
            print("You are not alone. Beast eat you.")
            print("Game over. ^_^")
        elif choice.lower() == "yellow":
            print("YOU WIN!")
        else:
            print("This option does not exist.")
            print("Game over. ^_^")
    elif choice.lower() == "swim":
        print("You are attacked by piranhas.")
        print("Game over. ^_^")
    else:
        print("This option does not exist.")
        print("Game over. ^_^")
elif choice.lower() == "right":
    print("In the floor there is hole. You fell.")
    print("Game over. ^_^")
else:
    print("This option does not exist.")
    print("Game over. ^_^")
