# Constants
import random 
SPEED = random.randint(1, 10)
BODY_PARTS = ["leg", "chest", "head"]

# Stats initialization
def init_stats():
    return {
        "health": random.randint(5, 10),
        "defense": random.randint(5, 10),
        "attack": random.randint(5, 10),
        "perception": random.randint(5, 10),
        "endurance": random.randint(5, 10),
        "charisma": random.randint(5, 10),
        "speech": random.randint(5, 10),
        "intellect": random.randint(5, 10),
        "agility": random.randint(5, 10),
        "luck": random.randint(5, 10),
        "speed": SPEED
    }

# Character class assignment
def assign_class(character):
    if character == "1":
        return "Vault Dweller", init_stats()
    elif character == "2":
        return "Ghoul", init_stats()
    elif character == "3":
        return "Brotherhood Member", init_stats()
    elif character == "4":
        return "Raider", init_stats()
    else:
        return "Random Class", init_stats()

# Stat allocation
def allocate_stats(stats):
    add = 10
    print(f"You now have {add} points to allocate.")
    
    while add > 0:
        stat = input("What stat do you want to put your points into? ").lower()
        num1 = int(input(f"How many points do you want to add to {stat}? "))

        if stat in stats and num1 <= add:
            stats[stat] += num1
            add -= num1
            print(f"You have now got {stats[stat]} {stat} and have {add} points left to spend.")
        else:
            print("Invalid choice or points exceed remaining allocation.")
    
    return stats

# Drinking the Vitamin Drink
def vitamin_drink(stats):
    add = 5
    print(f"You drink the Vitamin Drink and feel energized. You have {add} points to allocate.")
    
    while add > 0:
        stat = input("What stat do you want to put your points into? ").lower()
        num1 = int(input(f"And how many points do you want to add to {stat}? "))

        if stat in stats and num1 <= add:
            stats[stat] += num1
            add -= num1
            print(f"You have now got {stats[stat]} {stat} and {add} points left to spend.")
        else:
            print("Invalid choice or points exceed remaining allocation.")
    
    return stats

# Vault encounter
def vault(stats):
    print("You encounter a vault. Do you go inside?")
    vault_choice = input("Make your selection here: ").lower()
    
    if vault_choice in ["yes", "y"]:
        print("You enter the vault and face a fork. Left (room) or right (corridor)?")
        vault_choice1 = input("Please enter your decision here: ").lower()

        if vault_choice1 in ["left", "room"]:
            print("You step on a pressure plate. A bullet shoots toward you.")
            hit_location = random.choice(BODY_PARTS)
            base_dmg = random.randint(1, 25)

            if hit_location == "leg":
                damage_multiplier = 0.75
            elif hit_location == "chest":
                damage_multiplier = 1.0
            else:  # head
                damage_multiplier = 1.25

            dmg = base_dmg * damage_multiplier
            print(f"You took {dmg} damage, and you were hit in the {hit_location}.")

            if stats["health"] > dmg:
                stats["health"] -= dmg
                print(f"You survived! You now have {stats['health']} health.")
            else:
                print("You died.")
                exit()
    return stats

# Main game
def main():
    print("Welcome to FallouTwoD")
    character = input("Choose a character: 1 for Vault Dweller, 2 for Ghoul, 3 for Brotherhood, 4 for Raider, or Random for a random class: ").lower()

    if character == "random":
        character = str(random.randint(1, 4))

    character_class, stats = assign_class(character)

    print(f"You have selected a {character_class}")
    for stat, value in stats.items():
        print(f"{stat.capitalize()}: {value}")

    # Allocate points to stats
    stats = allocate_stats(stats)

    # Encounter the vault
    stats = vault(stats)

if __name__ == "__main__":
    main()
