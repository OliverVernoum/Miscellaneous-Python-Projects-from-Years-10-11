import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def start_game():
    print_slow("Welcome to Breaking Blocks: A Text-Based Adventure!")
    print_slow("You are Walter 'Block' White, a chemistry teacher turned Minecraft inventor.")
    print_slow("Your goal is to create the ultimate invention while avoiding danger.")
    main_menu()

def main_menu():
    print("\nWhat would you like to do?")
    print("1. Gather resources")
    print("2. Build an invention")
    print("3. Trade with villagers")
    print("4. Exit game")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        gather_resources()
    elif choice == "2":
        build_invention()
    elif choice == "3":
        trade_with_villagers()
    elif choice == "4":
        print_slow("Goodbye, inventor!")
        exit()
    else:
        print("Invalid choice. Try again.")
        main_menu()

def gather_resources():
    print_slow("\nYou head out to gather resources.")
    print_slow("You find some redstone, iron, and a mysterious blue crystal.")
    print_slow("The blue crystal seems... special.")
    main_menu()

def build_invention():
    print("\nWhat would you like to build?")
    print("1. Redstone contraption")
    print("2. Iron golem")
    print("3. Mysterious blue crystal machine")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print_slow("\nYou build a complex redstone contraption. It's impressive!")
    elif choice == "2":
        print_slow("\nYou create an iron golem to protect your base.")
    elif choice == "3":
        print_slow("\nYou use the mysterious blue crystal to build a strange machine.")
        print_slow("It hums with energy... but something feels off.")
    else:
        print("Invalid choice. Try again.")
        build_invention()
    main_menu()

def trade_with_villagers():
    print_slow("\nYou visit a nearby village to trade.")
    print_slow("The villagers are interested in your blue crystal.")
    print("\nWhat would you like to do?")
    print("1. Trade the blue crystal for emeralds")
    print("2. Keep the blue crystal")
    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        print_slow("\nYou trade the blue crystal for a pile of emeralds.")
        print_slow("The villagers seem thrilled, but you feel like you lost something important.")
    elif choice == "2":
        print_slow("\nYou decide to keep the blue crystal. The villagers seem disappointed.")
    else:
        print("Invalid choice. Try again.")
        trade_with_villagers()
    main_menu()

# Start the game
start_game()