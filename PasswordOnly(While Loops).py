lock=3

correct_password="Password123"

user_password = input( "Please enter a password: ")

while user_password != correct_password:
    user_password=input("Incorrect. Try again: ")
    lock=lock-1

if user_password == correct_password:
    print("Correct.")

if lock == 0:
    print("Too many failed attempts. Goodbye.")
