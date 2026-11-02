import random


dice_roll=random.randint(1,6)


print("You rolled a...",dice_roll,"")

if dice_roll <3:
    print("Low roll!")


elif dice_roll <6:
    print("Good roll!")

elif dice_roll==6:
    print("Amazing roll!")
    
