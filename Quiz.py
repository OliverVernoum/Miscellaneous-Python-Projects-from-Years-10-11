import random

print("Welcome to the Quiz")
print("remember to use correct capitalisation")

score=0

Ans1=input("What continent is Argentina in?")
if Ans1==("South America"):
    print ("Correct!")
    score=score+1

else:
    print("Wrong!")




Ans2=input("What book is Sun Wukong from?")
if Ans2==("Journey to the West"):
    print ("Correct!")
    score=score+1

else:
    print("Wrong!")








Ans3=input("What country is currently ruled by King Charles III")
if Ans3==("England"):
    print ("Correct!")
    score=score+1

else:
    print("Wrong!")





Ans4=input("What is the most popular soda brand in the U.S?")
if Ans4==("Coca Cola"):
    print ("Correct!")
    score=score+1

else:
    print("Wrong!")





Ans5=input("1664 x 10")                                                     
if Ans5==("16,640"):
    print ("Correct!")
    score=score+1

else:
    print("Wrong!")





Ans6=input("What political party is Nigel Farage in?")
if Ans6==("Reform UK"):
    print ("Correct!")
    score=score+1

else:
    print("Wrong!")




Ans7=input("Name the biggest sporting event that takes place every 4 years")
if Ans7==("The Olympics"):
    print ("Correct!")
    score=score+1

else:
    print("Wrong!")









Ans8=input("True or False? Donald Trump was assassinated on July 13th 2024")
if Ans8==("False"):
    print ("Correct!")
    score=score+1

else:
    print("Wrong!")





Ans9=input("Who wrote The Lord of The Rings Trilogy")
if Ans9==("JRR Tolkien"):
    print ("Correct!")
    score=score+1

else:
    print("Wrong!")






AnsX=input("What is the local Cryptid of New Delhi")
if AnsX==("Monkey Man"):
    print ("Correct!")
    score=score+1

elif AnsX==("Monkeyman"):
    print ("Correct!")
    score=score+1

else:
    print("Wrong!")




if score==1 or score==2 or score==3 or score==4 or score==5:
    print("You got ",(score)," Do better next time!")

elif score==6 or score==7 or score==8:
    print("You achieved ",(score)," Well done!")


elif score==9 or score==10:
    print("You managed to get ",(score),"! Astounding!")



