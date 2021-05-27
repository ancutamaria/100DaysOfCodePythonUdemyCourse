import art
import data
import random

current_score = 0
print(art.logo)
while True:
    celebrityA = random.choice(data.data)
    celebrityB = random.choice(data.data)
    while celebrityA.get("name") == celebrityB.get("name"):
        celebrityB = random.choice(data.data)

    print(f"Compare A: ")
    print(f"{celebrityA.get('name')}, a {celebrityA.get('description')}, from {celebrityA.get('country')}")
    print(art.vs)
    print(f"Compare B: ")
    print(f"{celebrityB.get('name')}, a {celebrityB.get('description')}, from {celebrityB.get('country')}")
    print()
    response = input("Who has more followers? Type 'A' or 'B': ")
    hasAmoreFollowersThanB = celebrityA.get("follower_count") > celebrityB.get("follower_count")
    print(art.logo)
    print()
    if hasAmoreFollowersThanB and response == "A":
        current_score += 1
        print(f"You're write! Current score: {current_score}.")
    elif not hasAmoreFollowersThanB and response == "B":
        current_score += 1
        print(f"You're write! Current score: {current_score}.")
    else:
        current_score = 0
        print(f"Sorry, that's wrong. Current score: 0")
    print()
