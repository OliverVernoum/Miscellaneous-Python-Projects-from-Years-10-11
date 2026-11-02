import random

ranumb=random.randint(1,100)
guessnum=0

print("Welcome to the Random Number Guesser")

guess=int(input("Please make your guess between 1 and 100: "))
while guess!=ranumb:
    guessnum=guessnum+1
    if guess>=ranumb:
        print("Wrong! Too high. Try again.")

    elif guess<=ranumb:
        print("Wrong! Too low. Try again.")

    else:
        print("ERR")

    guess=float(input("Guess Again: "))


if guess == ranumb:
    guessnum == guessnum + 1
    print("Congrats! It was",ranumb,". You made",guessnum,"guesses!")
    


