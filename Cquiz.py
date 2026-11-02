import random
questionum=0
maxnum=int(input("How many questions do you want? "))-1
score=0
while questionum <= maxnum:
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    questionum = questionum + 1
    print(f"Question number {questionum}")
    ans=int(input(f"What is {num1} + {num2}? "))
    if ans == num1 + num2:
            print("Correct!")
            score = score+1
    else:
        print("Wrong")
print(f" You scored {score} out of {maxnum}")
