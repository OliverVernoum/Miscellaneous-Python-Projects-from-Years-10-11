#FALLOUTWOD

import random
SPEED=random.randint(1,10)
BODY_PARTS=["leg","chest","head"]
events=[Vault,]

print("Welcome to FallouTwoD")
name=input("Enter a name: ")
character = input(f"Welcome,{name}. Please type 1 for a vault dweller, 2 for a Ghoul, 3 for a Brotherhood member, 4 for a Raider, and type Random for a random class: ")

def NukaCola():
    add=5
    print("You have found a drink on the ground. You drink the delicious Nuka-Cola and feel a surge of energy. You have",add," energy to allocate")
    while add !=0:
        if add<=0 or add<=5:
            stat=input("What stat do you want to put your points into? ")
            num1=int(input("And how many points do you want to add? "))

            if stat.lower()==("attack"):
                    attack=attack+num1
                    add=add-num1
                    print("You have now got",attack,"attack and have ",add,"energy left to spend.")

            elif stat.lower()==("attack"):
                    attack=attack+num1
                    add=add-num1
                    print("You have now got",attack,"attack and have ",add,"energy left to spend.")

            elif stat.lower()==("defense"):
                    defense=defense+num1
                    add=add-num1
                    print("You have now got",defense,"defense and have ",add,"energy left to spend.")

            elif stat.lower()==("health"):
                    health=health+num1
                    add=add-num1
                    print("You have now got",health,"health and have ",add,"energy left to spend.")

            elif stat.lower()==("perception"):
                        Perception=Perception+num1
                        add=add-num1
                        print("You have now got",Perception,"perception and have ",add,"energy left to spend.")

            elif stat.lower()==("endurance"):
                        Endurance=Endurance+num1
                        add=add-num1
                        print("You have now got",Endurance,"endurance and have ",add,"energy left to spend.")

            elif stat.lower()==("charisma"):
                        Charisma=Charisma+num1
                        add=add-num1
                        print("You have now got",Charisma,"charisma and have ",add,"energy left to spend.")

            elif stat.lower()==("speech"):
                        Speech=Speech+num1
                        add=add-num1
                        print("You have now got",Speech,"speech and have ",add,"energy left to spend.")

            elif stat.lower()==("intellect"):
                        Intellect=Intellect+num1
                        add=add-num1
                        print("You have now got",Intellect,"intellect and have ",add,"energy left to spend.")

            elif stat.lower()==("agility"):
                        Agility=Agility+num1
                        add=add-num1
                        print("You have now got",Agility,"agility and have ",add,"energy left to spend.")

            elif stat.lower()==("luck"):
                        Luck=Luck+num1
                        add=add-num1
                        print("You have now got",Luck,"luck and have ",add,"energy left to spend.")

            elif stat.lower()==("speed"):
                        SPEED=SPEED+num1
                        add=add-num1
                        print("You have now got",SPEED,"speed and have ",add,"energy left to spend.")

        print("Your new stats are as following")
        print("Health:", health)
        print("Defense:", defense)
        print("Attack:", attack)
        print("Perception:", Perception)
        print("Endurance:", Endurance)
        print("Charisma:", Charisma)
        print("Speech:", Speech)
        print("Intellect:", Intellect)
        print("Agility:", Agility)
        print("Luck:", Luck)
        print("Speed:",SPEED)



def Vault():
        global health
        print("You encounter a vault. Do you go inside?")
        vault_choice = input("Make your selection here: ").lower()
    
        if vault_choice.lower() in ["yes", "y"]:
         print("You enter the vault and face a fork. Left (room) or right (corridor)?")
         vault_choice1 = input("Please enter your decision here: ").lower()

        if vault_choice1.lower() in ["left", "room"]:
            print("You step on a pressure plate. A bullet shoots toward you.")
            hit_location = random.choice(BODY_PARTS)
            base_dmg = random.randint(1, 25)

            if hit_location == "leg":
                damage_multiplier = 0.75
            elif hit_location == "chest":
                damage_multiplier = 1.0
            else:  
                damage_multiplier = 1.25

            dmg = base_dmg * damage_multiplier
            print(f"You took {dmg} damage, and you were hit in the {hit_location}.")

            if health > dmg:
                health -= dmg
                print(f"You survived! You now have {health} health.")
            else:
                print("You died.")
                exit()

        elif vault_choice1.lower() in ["right", "corridor"]:
            print ("You come across three doors")
            choice_vault_corridor_doors=input("What door do you want to go through? Enter it here: ")

if character.lower() == "random":
    character = str(random.randint(1, 4))


if character == "1":
       character_class = "Vault Dweller"
elif character == "2":
       character_class = "Ghoul"
elif character == "3":
       character_class = "Brotherhood Member"
elif character == "4":
       character_class = "Raider"
        



if character=="1" or character_class== "Vault Dweller":
    character_class= "Vault Dweller"
    Speech = random.randint(5,10)
    health = random.randint(5,10)
    defense = random.randint(5,10)
    attack = random.randint (5,10)
    Perception = random.randint(5,10)
    Endurance = random.randint(5,10)
    Charisma = random.randint (5,10)
    Intellect = random.randint(5,10)
    Agility = random.randint(5,10)
    Luck = random.randint (5,10)
    
elif character=="2":
    character_class="Ghoul"
    Speech = random.randint(5,10)
    health = random.randint(5,10)
    defense = random.randint(5,10)
    attack = random.randint (5,10)
    Perception = random.randint(5,10)
    Endurance = random.randint(5,10)
    Charisma = random.randint (5,10)
    Intellect = random.randint(5,10)
    Agility = random.randint(5,10)
    Luck = random.randint (5,10)
            
    
    
elif character=="3":
    character_class="Brotherhood Member"
    Speech = random.randint(5,10)
    health = random.randint(5,10)
    defense = random.randint(5,10)
    attack = random.randint (5,10)
    Perception = random.randint(5,10)
    Endurance = random.randint(5,10)
    Charisma = random.randint (5,10)
    Intellect = random.randint(5,10)
    Agility = random.randint(5,10)
    Luck = random.randint (5,10)
    
elif character=="4":
    character_class= "Raider"
    Speech = random.randint(5,10)
    health = random.randint(5,10)
    defense = random.randint(5,10)
    attack = random.randint (5,10)
    Perception = random.randint(5,10)
    Endurance = random.randint(5,10)
    Charisma = random.randint (5,10)
    Intellect = random.randint(5,10)
    Agility = random.randint(5,10)
    Luck = random.randint (5,10)

# Output character details
print("You have selected a", character_class)
print("Health:", health)
print("Defense:", defense)
print("Attack:", attack)
print("Perception:", Perception)
print("Endurance:", Endurance)
print("Charisma:", Charisma)
print("Speech:", Speech)
print("Intellect:", Intellect)
print("Agility:", Agility)
print("Luck:", Luck)
print("Speed:",SPEED)


add=10
print(f"You now have the opportunity to add to a stat of your choice. You have {add} points to spend")
while add !=0:
    stat=input ("What stat do you want to put your points into?") 
    num1=int(input("And how many points do you want to add? ")) 
    if stat. lower ()==("attack"):
        attack+=num1
        add-=num1
        print("You have now got", attack, "attack and have ",add, "points left to spend.")
    elif stat.lower()==("attack"):
        attack=attack+num1
        add=add-num1
        print("You have now got", attack, "attack and have ",add,"points left to spend.")
    elif stat. lower()==("defense"):
        defense=defense+num1
        add=add-num1
        print("You have now got",defense, "defense and have " , add, "points left to spend.")
    elif stat. lower ()==("health"):
        health=health+num1
        add=add-num1
        print("You have now got",health, "health and have " , add, "points left to spend.")
        
    elif stat.lower()==("perception"):
        Perception=Perception+num1
        add=add-num1
        print("You have now got",Perception,"perception and have ",add,"points left to spend.")
        
    elif stat.lower()==("endurance"):
        Endurance=Endurance+num1
        add=add-num1
        print("You have now got",Endurance,"endurance and have ",add,"points left to spend.")
        
    elif stat.lower()==("charisma"):
        Charisma=Charisma+num1
        add=add-num1
        print("You have now got",Charisma,"charisma and have ",add,"points left to spend.")

    elif stat.lower()==("speech"):
            Speech=Speech+num1
            add=add-num1
            print("You have now got",Speech,"speech and have ",add,"points left to spend.")

    elif stat.lower()==("intellect"):
            Speech=Speech+num1
            add=add-num1
            print("You have now got",Speech,"speech and have ",add,"points left to spend.")

    elif stat.lower()==("agility"):
            Speech=Speech+num1
            add=add-num1
            print("You have now got",Speech,"speech and have ",add,"points left to spend.")

    elif stat.lower()==("luck"):
            Speech=Speech+num1
            add=add-num1
            print("You have now got",Speech,"speech and have ",add,"points left to spend.")

    elif stat.lower()==("speed"):
            Speech=Speech+num1
            add=add-num1
            print("You have now got",Speech,"speech and have ",add,"points left to spend.")

    else:
        print("Invalid. Please try again")





print(f"{name},Your new stats are as following")
print("Health:", health)
print("Defense:", defense)
print("Attack:", attack)
print("Perception:", Perception)
print("Endurance:", Endurance)
print("Charisma:", Charisma)
print("Speech:", Speech)
print("Intellect:", Intellect)
print("Agility:", Agility)
print("Luck:", Luck)
print("Speed:",SPEED)


if character_class == "Vault Dweller":
    print(f"Welcome,{name}, the Vault Dweller. You wake up in Vault 69 after a busy day and night. You check your water system. To your shock and horror,you discover the chip is fried. You need a new one. You get your suit and kiss your 345 girlfriends goodbye, and set out into the great unknown.")

elif character_class == "Brotherhood Member":
    



     
