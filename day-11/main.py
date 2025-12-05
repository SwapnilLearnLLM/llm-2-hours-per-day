import random
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_cards(cards):
    """Take a list of cards and return the score calcuated"""
    if sum(cards) == 2 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(u_score, d_score):
    if u_score == d_score:
        return "It's a DRAW :)"
    elif d_score == 0:
        return "Lose, Opponent has a blackjack"
    elif u_score == 0:
        return "Win with a Black Jack"
    elif u_score > 21:
        return "You went Over. You Loose"
    elif u_score > d_score:
        return "You Win."
    else:
        return "You Loose."
def play_game():
    print(logo)
    user_cards = []
    dealer_cards = []
    is_game_Over = False
    dealer_score = -1
    user_score = -1



    for _ in range(2):
        # new_card = deal_card()
        # user_cards.append(new_card)
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_Over:
        user_score = calculate_cards(user_cards)
        dealer_score = calculate_cards(dealer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_Over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_Over = True
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_cards(dealer_cards)

    print(f"Your final Hand : {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score} ")
    print(compare(user_score, dealer_score))



while input("Do you wanna play a game of BlackJack? Type 'y' or 'n' : ") == "y":
    print("\n" *20)
    play_game()