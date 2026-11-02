# # Cracking Christmas ##

# Imports libraries that will be used
import time
import random
import winsound
choice1 = "Err"

# Adds a typewriter effect to every print statement
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
        if char == ",":
            time.sleep(0.5)
        if char == ".":
            time.sleep(0.25)
    print()

def print_slower(text):
    winsound.PlaySound(r"c:\Users\olive\OneDrive - Hull Collegiate School\Year 10 Computing\Python\zelda-chest-opening-and-item-catch.wav", winsound.SND_FILENAME)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.3)
        
    print()

# Adds a typewriter effect to every input
def input_slow(prompt):
    for char in prompt:
        print(char, end='', flush=True)
        time.sleep(0.05)
        if char == ",":
            time.sleep(0.5)
        if char == ".":
            time.sleep(0.25)
    return input()



print_slow("Welcome to Santa's Workshop. In the past couple years, Santa has decided to catch up with the modern age and has digitised a lot of his workshop. Half of his elves now work from home. And you have been hired as Santa's IT technician. There's one problem with that though, you know absolutely nothing about IT." )
print_slow("Your mission, should you choose to accept it, is to learn on the job about different IT terminology, in order to stop the Grinch from hacking Christmas.") 
name = input_slow("Now, what is your name? ")
print_slow(f"Welcome, {name}. You open your eyes after a quick powernap to find yourself sat at your desk in the grotto. There are two windows open on your desktop.")

while choice1 not in ["naughty", "nice"] :
    choice1 = input_slow("Do you want to open the file labelled 'Naughty List' or the file labelled 'Nice List'? Type 'Naughty' or 'Nice' here:  ").lower()
    if choice1 == "naughty":
        print_slow("You open the folder to discover a file called 'Array.txt'. You click the file and it says the following.")
        print_slow("An array is a series of memory locations or 'boxes' each of which holds a single item of data, but with each box sharing the same collective name. All data in an array must be of the same data type")
        print_slower("You learned what an Array is!")
        

    elif choice1 == "nice":
        print_slow("You open the folder to discover a file called 'Cloud.txt'. You click the file and it says the following.")
        print_slow("The cloud is a network of remote servers hosted on the internet to store, manage, and process data, rather than a local server or a personal computer. Examples of cloud services include Google Drive, iCloud, and Dropbox.")
        print_slower("You learned what The Cloud is!")
