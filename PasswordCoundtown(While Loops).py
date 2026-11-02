import time

correct_password="Password123"

user_password=input("Please enter a password: ")

while user_password != correct_password:
    user_password=input("Incorrect. Try again: ")

while user_password == correct_password:

    print("It's countdowning time")
    number=100
    while number > 0:
        time.sleep(0.5)
        print (number)
        number=number-1
        if number == 0:
            print("I just countdowned everywhere")
            
    break 

