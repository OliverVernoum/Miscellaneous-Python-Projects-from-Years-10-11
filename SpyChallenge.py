agent_name = "Tim Cheese"
mission_objective = "Find the nearest McDonalds"
door_attempts = 0
doorcode_right = False
def revealsecrets():
    print("The nearest McDonalds is near Waitrose")
    print("You will find the target, John Pork, there. Neutralise him.")
    print("Good Luck.")
print(f"Your name is {agent_name} and your mission is to {mission_objective}")
HQmessage= input("Enter your message to HQ here: ")
print(f"HQ has recieved you message {HQmessage}")
print("HQ: Code for the door is 'opensesame'. Good luck")
while doorcode_right == False:
    doorcode = input("Enter the doorcode here: ")
    if doorcode.lower()=="opensesame":
        print("Well done! You guessed the door code correctly")
        doorcode_right = True
        revealsecrets() 
    else:
        print("ERR: Doorcode incorrect.")
        door_attempts += 1
        if door_attempts == 2:
            print("The hint is open______")
        if door_attempts == 3:
            print("The door blew up. ")
            break