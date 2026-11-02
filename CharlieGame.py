#Charlie's game#
import random
score = 0
Num1=random.randint(1,10)
Num2=random.randint(1,10)
Num3=random.randint(1,10)
Num4=random.randint(1,10)
Num5=random.randint(1,10)
Num6=random.randint(1,10)

Ans1=int(input(f"Question 1. What is {Num1} + {Num2}?"))
if Ans1 == Num1 + Num2:
    print("Correct!")
    score = score + 1
else:
    print ("Wrong!")

Ans2=int(input(f"Question 2. What is {Num3} + {Num4}?"))
if Ans2 == Num3 + Num4:
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

Ans3=int(input(f"Question 1. What is {Num5} + {Num6}?"))
if Ans3 == Num5 + Num6:
    print("Correct!")
    score = score + 1
else:
    print("Wrong")

print(f"You scored {score} points.")
    
