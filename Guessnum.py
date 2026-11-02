import random
guessed = False
guesses = 0
secret_num = random.randint(1,20)
print("I am thinking of a number between 1 and 20.")

while guessed == False:
    guess = int(input("Take a guess: "))
    if guess < 1 or guess > 20:
        print("Your guess is out of range. Please guess a number between 1 and 20.")
    elif guess < secret_num:
        print("Your guess is too low.")
        guesses += 1
    elif guess > secret_num:
        print("Your guess is too high.")
        guesses += 1

    
    else:
        print(f"Well done! You guessed my number! You took {guesses} guesses.")
        guessed = True