#FALLOUTWOD

import random

print("Welcome to FallouTwoD")

character = intinput("Welcome, Please type 1 for a vault dweller, 2 for a Ghoul, 3 for a Brotherhood member, 4 for a Raider, and type 5 for a random class: ")


if character ==("5"):
	character =random.randint(1,4)

Speech = health = defense = attack = Perception = Endurance = Charisma = Intellect = Agility = Luck = 0


if character == "1":
    character_class = "Vault Dweller"
elif character == "2":
    character_class = "Ghoul"
elif character == "3":
    character_class = "Brotherhood Member"
elif character == "4":
    character_class = "Raider"
else:
    print("Invalid selection")
    character_class = None

if character_class:
    Speech = random.randint(5, 10)
    health = random.randint(5, 10)
    defense = random.randint(5, 10)
    attack = random.randint(5, 10)
    Perception = random.randint(5, 10)
    Endurance = random.randint(5, 10)
    Charisma = random.randint(5, 10)
    Intellect = random.randint(5, 10)
    Agility = random.randint(5, 10)
    Luck = random.randint(5, 10)

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

add=5

print("You now have the opportunity")

