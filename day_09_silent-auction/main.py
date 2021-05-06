import art

bidders = []

while True:
    print(art.logo)
    print("Welcome to the secret auction program.")
    name = input("What is your name? ")
    amount = int(input("What is your bid? "))
    bidders.append({"name": name, "amount": amount})
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bidders == "no":
        winner = {"name": "", "amount": -1}
        for bidder in bidders:
            if bidder["amount"] > winner["amount"]:
                winner = {"name": bidder["name"], "amount": bidder["amount"]}
        print(f"The winner is: {winner['name']}")
        break
    elif other_bidders == "yes":
        print('\n' * 100)

