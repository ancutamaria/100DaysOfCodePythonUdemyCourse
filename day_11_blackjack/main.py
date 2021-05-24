import art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose. Computer has Blackjack"
    elif user_score == 0:
        return "Win. You have Blackjack"
    elif user_score > 21:
        return "Lose. You went over 21."
    elif computer_score > 21:
        return "Win. Computer went over 21."
    elif user_score > computer_score:
        return "Win."
    else:
        return "Lose."


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"user: {user_cards} and score: {user_score}")
        print(f"computer 1st card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type y or n if you want another card ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards} with score {user_score}")
    print(f"   Computer's final hand: {computer_cards} with score {computer_score}")

    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type y or n: ") == "y":
    print(art.logo)
    play_game()


