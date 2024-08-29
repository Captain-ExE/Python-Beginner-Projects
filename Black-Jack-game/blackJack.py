import random


def deal_card():
    """Generate random cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """take the list of cards and return the sum of cards list"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(usr_score, cptr_score):
    if usr_score == cptr_score:
        return "It's a draw."
    elif cptr_score == 0:
        return "You lose. opponent has Blackjack!"
    elif usr_score == 0:
        return "You Win with a Blackjack!"
    elif usr_score > 21:
        return "You lose! you went  over."
    elif cptr_score > 21:
        return "You Win. computer has went over."
    elif usr_score > cptr_score:
        return "You Win!"
    else:
        return "You lose."

def play_game():

    user_card = []
    computer_card = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    # Choose two random cards and add them to your_card list
    for card in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"your cards = {user_card} and current score = {user_score}")
        print(f"computer's first card = {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("type 'y' to get another card or type 'n' to pass: ")
            if user_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final cards: {user_card} total score: {user_score}")
    print(f"Computer's final cards: {computer_card} total score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play blackjack? type 'y' or 'n': ") == "y":
    play_game()

