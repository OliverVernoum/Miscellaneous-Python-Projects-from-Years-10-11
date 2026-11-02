#FALLOUTWOD
import time
import random
SPEED=random.randint(1,10)
BODY_PARTS=["leg","chest","head"]



def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def input_slow(prompt):
    for char in prompt:
        print(char, end='', flush=True)
        time.sleep(0.05)
    return input()

print_slow("Welcome to FallouTwoD")

character = input_slow("Welcome, Please type 1 for a vault dweller, 2 for a Ghoul, 3 for a Brotherhood member, 4 for a Raider, and type Random for a random class: ")

def VitaminDrink():
    add=5
    print_slow("You drink the delicious Vitamin Drink and feel a surge of energy. You have " + str(add) + " energy to allocate")
    while add !=0:
        if add<=0 or add<=5:
            stat=input_slow("What stat do you want to put your points into? ")
            num1=int(input_slow("And how many points do you want to add? "))

            if stat.lower()==("attack"):
                    attack=attack+num1
                    add=add-num1
                    print_slow("You have now got " + str(attack) + " attack and have " + str(add) + " energy left to spend.")

            elif stat.lower()==("attack"):
                    attack=attack+num1
                    add=add-num1
                    print_slow("You have now got " + str(attack) + " attack and have " + str(add) + " energy left to spend.")

            elif stat.lower()==("defense"):
                    defense=defense+num1
                    add=add-num1
                    print_slow("You have now got " + str(defense) + " defense and have " + str(add) + " energy left to spend.")

            elif stat.lower()==("health"):
                    health=health+num1
                    add=add-num1
                    print_slow("You have now got " + str(health) + " health and have " + str(add) + " energy left to spend.")

            elif stat.lower()==("perception"):
                        Perception=Perception+num1
                        add=add-num1
                        print_slow("You have now got " + str(Perception) + " perception and have " + str(add) + " energy left to spend.")

            elif stat.lower()==("endurance"):
                        Endurance=Endurance+num1
                        add=add-num1
                        print_slow("You have now got " + str(Endurance) + " endurance and have " + str(add) + " energy left to spend.")

            elif stat.lower()==("charisma"):
                        Charisma=Charisma+num1
                        add=add-num1
                        print_slow("You have now got " + str(Charisma) + " charisma and have " + str(add) + " energy left to spend.")

            elif stat.lower()==("speech"):
                        Speech=Speech+num1
                        add=add-num1
                        print_slow("You have now got " + str(Speech) + " speech and have " + str(add) + " energy left to spend.")

            elif stat.lower()==("intellect"):
                        Intellect=Intellect+num1
                        add=add-num1
                        print_slow("You have now got " + str(Intellect) + " intellect and have " + str(add) + " energy left to spend.")

            elif stat.lower()==("agility"):
                        Agility=Agility+num1
                        add=add-num1
                        print_slow("You have now got " + str(Agility) + " agility and have " + str(add) + " energy left to spend.")

            elif stat.lower()==("luck"):
                        Luck=Luck+num1
                        add=add-num1
                        print_slow("You have now got " + str(Luck) + " luck and have " + str(add) + " energy left to spend.")

            elif stat.lower()==("speed"):
                        SPEED=SPEED+num1
                        add=add-num1
                        print_slow("You have now got " + str(SPEED) + " speed and have " + str(add) + " energy left to spend.")

        print_slow("Your new stats are as following")
        print_slow("Health: " + str(health))
        print_slow("Defense: " + str(defense))
        print_slow("Attack: " + str(attack))
        print_slow("Perception: " + str(Perception))
        print_slow("Endurance: " + str(Endurance))
        print_slow("Charisma: " + str(Charisma))
        print_slow("Speech: " + str(Speech))
        print_slow("Intellect: " + str(Intellect))
        print_slow("Agility: " + str(Agility))
        print_slow("Luck: " + str(Luck))
        print_slow("Speed: " + str(SPEED))



def Vault():
        global health
        print_slow("You encounter a vault. Do you go inside?")
        vault_choice = input("Make your selection here: ").lower()
    
        if vault_choice.lower() in ["yes", "y"]:
         print_slow("You enter the vault and face a fork. Left (room) or right (corridor)?")
         vault_choice1 = input("Please enter your decision here: ").lower()

        if vault_choice1.lower() in ["left", "room"]:
            print_slow("You step on a pressure plate. A bullet shoots toward you.")
            hit_location = random.choice(BODY_PARTS)
            base_dmg = random.randint(1, 25)

            if hit_location == "leg":
                damage_multiplier = 0.75
            elif hit_location == "chest":
                damage_multiplier = 1.0
            else:  
                damage_multiplier = 1.25

            dmg = base_dmg * damage_multiplier
            print_slow(f"You took {dmg} damage, and you were hit in the {hit_location}.")

            if health > dmg:
                health -= dmg
                print_slow(f"You survived! You now have {health} health.")
            else:
                print_slow("You died.")
                exit()

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
print_slow("You have selected a " + character_class)
print_slow("Health: " + str(health))
print_slow("Defense: " + str(defense))
print_slow("Attack: " + str(attack))
print_slow("Perception: " + str(Perception))
print_slow("Endurance: " + str(Endurance))
print_slow("Charisma: " + str(Charisma))
print_slow("Speech: " + str(Speech))
print_slow("Intellect: " + str(Intellect))
print_slow("Agility: " + str(Agility))
print_slow("Luck: " + str(Luck))
print_slow("Speed: " + str(SPEED))


add=10
print_slow(f"You now have the opportunity to add to a stat of your choice. You have {add} points to spend")
while add !=0:
    stat=input_slow ("What stat do you want to put your points into?") 
    num1=int(input_slow("And how many points do you want to add? ")) 
    if stat. lower ()==("attack"):
        attack+=num1
        add-=num1
        print_slow("You have now got " + str(attack) + " attack and have " + str(add) + " points left to spend.")
    elif stat.lower()==("attack"):
        attack=attack+num1
        add=add-num1
        print_slow("You have now got " + str(attack) + " attack and have " + str(add) + " points left to spend.")
    elif stat. lower()==("defense"):
        defense=defense+num1
        add=add-num1
        print_slow("You have now got " + str(defense) + " defense and have " + str(add) + " points left to spend.")
    elif stat. lower ()==("health"):
        health=health+num1
        add=add-num1
        print_slow("You have now got " + str(health) + " health and have " + str(add) + " points left to spend.")
        
    elif stat.lower()==("perception"):
        Perception=Perception+num1
        add=add-num1
        print_slow("You have now got " + str(Perception) + " perception and have " + str(add) + " points left to spend.")
        
    elif stat.lower()==("endurance"):
        Endurance=Endurance+num1
        add=add-num1
        print_slow("You have now got " + str(Endurance) + " endurance and have " + str(add) + " points left to spend.")
        
    elif stat.lower()==("charisma"):
        Charisma=Charisma+num1
        add=add-num1
        print_slow("You have now got " + str(Charisma) + " charisma and have " + str(add) + " points left to spend.")

    elif stat.lower()==("speech"):
            Speech=Speech+num1
            add=add-num1
            print_slow("You have now got " + str(Speech) + " speech and have " + str(add) + " points left to spend.")

    elif stat.lower()==("intellect"):
            Speech=Speech+num1
            add=add-num1
            print_slow("You have now got " + str(Intellect) + " intellect and have " + str(add) + " points left to spend.")

    elif stat.lower()==("agility"):
            Speech=Speech+num1
            add=add-num1
            print_slow("You have now got " + str(agility) + " agility and have " + str(add) + " points left to spend.")

    elif stat.lower()==("luck"):
            Speech=Speech+num1
            add=add-num1
            print_slow("You have now got " + str(luck) + " luck and have " + str(add) + " points left to spend.")

    elif stat.lower()==("speed"):
            Speech=Speech+num1
            add=add-num1
            print_slow("You have now got " + str(SPEED) + " speed and have " + str(add) + " points left to spend.")

    else:
        print_slow("Invalid. Please try again")





print_slow("Your new stats are as following")
print_slow("Health: " + str(health))
print_slow("Defense: " + str(defense))
print_slow("Attack: " + str(attack))
print_slow("Perception: " + str(Perception))
print_slow("Endurance: " + str(Endurance))
print_slow("Charisma: " + str(Charisma))
print_slow("Speech: " + str(Speech))
print_slow("Intellect: " + str(Intellect))
print_slow("Agility: " + str(Agility))
print_slow("Luck: " + str(Luck))
print_slow("Speed: " + str(SPEED))




def GameStart():
    print_slow("Welcome to FallouTwoD")
    print_slow("You are a vault dweller in a post-apocalyptic world.")
    print_slow("You wake up to start the day. You go to your tap and turn it on. To your horror, nothing comes out. You know what you must do.")
    print_slow("What do you decide to do? Do you: Search your home vault for water, journey into the wasteland, or arrange a meeting with the vault supervisor?")
    Choice1=input("Please enter your choice here: ").lower()
    if Choice1.lower() in ["search", "home vault"]:
        print_slow("You search your home vault for water.")
        print_slow("You find a bottle of water.")
        print_slow("You drink the water and feel refreshed.")
        VitaminDrink()
    elif Choice1.lower() in ["journey", "wasteland"]:
        print_slow("You journey into the wasteland.")
        Vault()
    elif Choice1.lower() in ["arrange", "meeting", "vault supervisor"]:
        print_slow("You arrange a meeting with the vault supervisor.")
    else:
        print_slow("Invalid choice. Please try again.")
        GameStart()




GameStart()
