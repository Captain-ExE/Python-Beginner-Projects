import random
from art import logo, vs
from game_data import data


def acc_format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."

def check_answer(user_input, a, b):
    if a>b:
        return user_input == "a"
    else:
        return user_input == "b"

# Display art
print(logo)
print("--- Welcome to the Higher Lower Game ---\n\n")
score = 0
is_continue = True
account_b = random.choice(data)
while is_continue :
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {acc_format(account_a)}")
    print(vs)
    print(f"Against B: {acc_format(account_b)}")

    #Ask user for a guess
    guess = input("Who has more followers? type 'A' or 'B': ").lower()
    #Check user is correct

    ##get user count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    #give user feedback on their guess
    if is_correct:
        score+=1
        print(f"Yes you are correct! current score: {score}\n\n")
    else:
        print(f"You are wrong! Final score: {score}\n\n")
        is_continue = False
