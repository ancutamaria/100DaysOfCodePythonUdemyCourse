import data

on = True
water_left = data.resources.get("water")
milk_left = data.resources.get("milk")
coffee_left = data.resources.get("coffee")
money_left = 0.0
quarter = 0.25
dime = 0.1
nickel = 0.05
penny = 0.01


def evaluate_option(option):
    global water_left
    global milk_left
    global coffee_left
    global money_left
    global quarter
    global dime
    global nickel
    global penny
    if data.MENU.get(option).get("ingredients").get("water") <= water_left:
        if data.MENU.get(option).get("ingredients").get("milk") <= milk_left:
            if data.MENU.get(option).get("ingredients").get("coffee") <= coffee_left:
                print(f"One {option} costs {data.MENU.get(option).get('cost')}$.")
                print("\nInsert coins:")
                q = int(input(" - number of quarters: "))
                d = int(input(" - number of dimes: "))
                n = int(input(" - number of nickels: "))
                p = int(input(" - number of pennies: "))
                money_left = q*quarter + d*dime + n*nickel + p*penny
                print(f"\nYou inserted {money_left}$")
                if data.MENU.get(option).get("cost") > money_left:
                    print("\nSorry, there is not enough money. Money refunded.\n")
                else:
                    money_left -= data.MENU.get(option).get("cost")
                    if money_left > 0:
                        print(f"Here is ${money_left} in change.")
                    money_left = 0.0
                    water_left -= data.MENU.get(option).get("ingredients").get("water")
                    milk_left -= data.MENU.get(option).get("ingredients").get("milk")
                    coffee_left -= data.MENU.get(option).get("ingredients").get("coffee")
                    print(f"Here is your {option}. Enjoy! ☕\n")
            else:
                print("\nSorry, there is not enough coffee.")
        else:
            print("\nSorry, there is not enough milk.\n")
    else:
        print("\nSorry, there is not enough water.\n")


while on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    if choice == "espresso":
        evaluate_option("espresso")
    elif choice == "latte":
        evaluate_option("latte")
    elif choice == "cappuccino":
        evaluate_option("cappuccino")
    elif choice == "off":
        on = False
        print()
        print("The machine is now turned off. Have a good day!")
    elif choice == "report":
        print(f"\nWater: {water_left}ml")
        print(f"Milk: {milk_left}ml")
        print(f"Coffe: {coffee_left}g")
        print(f"Money: ${money_left}\n")
    else:
        print("\nThis option is not valid. Please try again\n")
