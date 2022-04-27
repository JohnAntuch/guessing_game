secret_word = "John"
Guess = ""

guess_counter = 0
guess_limit = 3
out_of_guess = False

while Guess != secret_word and not(out_of_guess):
    if guess_counter < guess_limit:
        Guess = input("Enter a word: ")
        guess_counter += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Loser")
else:
    print("You win!")
