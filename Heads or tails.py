import random
coin=0
head_tail=random.randint(1,2)
print("",head_tail,"")
guess=input("Hello. Heads or Tails?")
if guess==("heads") or ("Heads"):
    coin==1

elif guess==("tails") or ("Tails"):
    coin==2
      
if head_tail==coin:
        print("Congratulations! It was ",guess,"")



else:
    restart=input("You failed! Try again? Type Y for Yes and N for No. ")


if restart==("Y"):
    print("This feature is currently under development. Please restart the program manually")


else:
    print("Thanks for Playing!")
    
