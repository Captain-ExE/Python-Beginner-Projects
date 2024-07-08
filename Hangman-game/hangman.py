import random
from hangman_art import stages
from wordList import word_list

print(
    "Welcome to the Hangman game. here you have to save the game by guessing correct word.\n"
)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)
print("the hidden word is")

display = []
for _ in range(word_length):
    display += "_"
print(*display, sep=' ')
print("\n")
life = 6
end_game = False
while not end_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess
    print(*display, sep=' ')
    print("\n")
    if "_" not in display:
        end_game = True
        print("You win!")
        print(f'The word is "{chosen_word}"')

    if guess not in chosen_word:
        life -= 1
        print(f"You lost one life.  current life: {life}")
        print(stages[life])
        if life == 0:
            print("\n!!! You lose !!!")
