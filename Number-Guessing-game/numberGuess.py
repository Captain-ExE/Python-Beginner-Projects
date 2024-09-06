import random
EASY_LVL = 10
HARD_LVL = 5

# Function to check users' guess against actual answer

def check_ans(user_guess, actual_number, turns):
    """Compare and return the number of turns"""
    diff = 0
    if user_guess > actual_number:
        diff = user_guess - actual_number
        if diff >= 1 and diff <= 10:
            print("little high")
            return turns - 1
        elif diff > 11:
            print("Too high")
            return turns - 1
    elif user_guess < actual_number:
        diff = actual_number - user_guess
        if diff >= 1 and diff <= 10:
            print("little low")
            return turns - 1
        elif diff > 11:
            print("Too low")
            return turns - 1
    else:
        print(f"You got it! The actual answer is: {actual_number}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LVL
    else:
        return HARD_LVL

def game():
    # Choosing a random number between 1 and 100.
    print("--- Welcome to the Number Guessing Game ---")
    print("I am thinking of a number between 1 to 100")
    answer = random.randint(1,100)
    # print(f"The answer is : {answer}")
    # You can turn on this print statement for test purpose.
    turns = set_difficulty()
    guess = 0
    # Repeat the guessing functionality if they get it wrong.
    while guess != answer:
        print(f"you have {turns} number of chances to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_ans(guess, answer, turns)
        if turns == 0:
            print("you run out of chances. You lose.")
            return

game()
