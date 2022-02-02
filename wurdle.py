import random
import json

class colours:
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'

def take_guess(num_guess, dictionary):
    while True:
        guess = input(f"Guess {num_guess}: ")
        if len(guess) == 5 and guess in dictionary:
            return guess
        else:
            print("Guess must be a 5 letter word, try again.")

def success_message(guesses):
    if guesses == 1:
        print("Amazing, it's your lucky day!")
    elif guesses == 2:
        print("Magnificent!")
    elif guesses == 3:
        print("Very cool, well done!")
    elif guesses == 4:
        print("Good effort!")
    elif guesses == 5:
        print("Pretty good.")
    elif guesses == 6:
        print("Got there!")

with open("wurdle_dict.json") as f:
    not_sols = json.load(f)
with open("wurdle_sols.json") as f:
    solutions = json.load(f)
dictionary = not_sols + solutions
the_word = random.choice(solutions)

not_in = ""
max_guesses = 6
share = []
print(f"You have {max_guesses} guesses...")
for g in range(1, max_guesses+1):
    guess = take_guess(g, dictionary)
    res = ""
    share_line = ""
    for i in range(len(guess)):
        if guess[i] == the_word[i]:
            res += colours.GREEN + guess[i].upper() + colours.ENDC
            share_line += colours.GREEN + "0" + colours.ENDC
        elif guess[i] in the_word and guess[i].upper() not in res:
            res += colours.YELLOW + guess[i].upper() + colours.ENDC
            share_line += colours.YELLOW + "0" + colours.ENDC
        else:
            res += guess[i].upper()
            share_line += "0"
            if guess[i].upper() not in not_in:
                not_in += guess[i].upper()
    print(res)
    share.append(share_line)
    if guess == the_word:
        success_message(g)
        print(f"{g}/{max_guesses}")
        for line in share:
            print(line)
        exit(0)
    if g == max_guesses:
        print(f"The word is {the_word.upper()}. Better luck next time.")
        exit(0)
    print(f"Other letters tried: {' '.join(not_in)}")
