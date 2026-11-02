import random


print("Welcome to the character creator.")

print("Please select a class. You can choose a Knight, Wizard, Rogue, or Nomad")

character=input("Please select 1 for a Knight, 2 for a Wizard, 3 for a Rogue, 4 for a Nomad or Random for a random class")
SPEED= random.randint(1,100)

if character.lower() == "random":
    character = str(random.randint(1, 4))


if character=="1":
    character_class= "Knight"
    health = random.randint(70,100)
    defense = random.randint(50,90)
    attack = random.randint (0,50)


elif character=="2":
    character_class= "Wizard"
    health = random.randint(5,50)
    defense = random.randint(30,70)
    attack = random.randint (70,100)


elif character=="3":
    character_class= "Rogue"
    health = random.randint(30,50)
    defense = random.randint(60,70)
    attack = random.randint (5,100)

elif character=="4":
    character_class= "Nomad"
    health = random.randint(0,100)
    defense = random.randint(0,100)
    attack = random.randint (0,100)
else:
    print("Wrong")

print("You have selected a ",character_class,"")
print("Health:",health,"")
print("Defense:",defense,"")
print("Attack:",attack,"")
print("Speed:",SPEED)



print("You have encountered an arrow.")

body_parts=["leg","chest","head"]
hit_location = random.choice(body_parts)
base_dmg=random.randint(1,25)

if hit_location == "leg":
            damage_multiplier = 0.75

elif hit_location == "chest":
    damage_multiplier = 1.0

elif hit_location == "head":
    damage_multiplier = 1.25

dmg=base_dmg*damage_multiplier

print("You took",dmg,"damage, and you were hit in the",hit_location,"")

if health > dmg:
    health= health-dmg
    print("You survived! You now have",health,"health")

else:
    print("You died.")
    exit()


#Coding Club 2
#Assaulting the Dragon's den

print("\nYou are approaching Max's hideout.")
print("Do you want to:")
print("1-Assault the main entrance")
print("2-Sneak around.")
print("3-Surrender")
choice=input("Input your decison here: ")
enemy_health=random.randint(30,35)
if choice == ("1"):
    print("You assault the main entrance")
    print("You spot a guard holding the key to the throne room. This is your chance.")
    Path1=input("""Will you:
1. Charge Him.
2.Throw a dagger
3.Sneak away""")
    if Path1=="1":
        attack1=random.randint(1,4)

    if attack1==1:
        print ("Attack Missed.")

    elif attack1==2 or 3:
        print("You did",attack,"damage")
        enemy_health=enemy_health-attack
        enemy_health=enemy_health-attack
    elif attack1==4:
        print("Critical hit!  You dealt",attack*2,"damage")
        enemy_health=enemy_health-attack*2

        

elif choice ==("2"):
    print("You sneak around the side")


elif choice ==("3"):
    print("Max looks at you and you die of his aura. He spews fire over your corpse")
    exit()
	




