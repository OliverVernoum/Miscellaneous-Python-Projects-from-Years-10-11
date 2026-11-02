import random


guessnum = 0
pass1 = random.choice(["sandwich","toastie","generation","database","password","cascade","zenith","luminous","whisper","embark","tangle","mirage","solstice","harbor","glimmer","fragrance","enigma","zephyr","mosaic","venture"])
passlength=len(pass1)

maxguess = 10
print("Welcome to the password guesser. You have 10 guesses.")
print(pass1)

while guessnum <= maxguess:
    guess = input("Enter your guess: ")

    if guess.lower() == pass1:
        print("Well done!")
        break


    else:
        guessnum = guessnum + 1

        print("Wrong!")

        if guessnum == 3:
            print(f"The length of the word is {passlength}")

        elif guessnum == 5:
            print(f"The first letter is {pass1[0]}")

        elif guessnum == 7:
            print(f"It's a nail biter! The 4th letter is {pass1.upper([3])}")
           

        elif guessnum == 9:
            print(f"Last chance! The last letter is {pass1.upper([-1])}")



if guessnum == maxguess:
    print(f"You lose! It was {pass1}")
    exit()


