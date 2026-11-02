# Buggy Python program for debugging practice

print("Welcome to the expanded program!")

# Ask the user for their name
name = input("What is your name? ")

# Input validation for age
while True:
    age = input("How old are you? ")
    if age.isdigit() and int(age) > 0:
        age = int(age)
        break
    else:
        print("Please enter a valid age (positive number).")

# Ask if the user knows their birth year
choice = input("Do you want to enter your birth year? (yes/no) ")

# If user knows their birth year, use it to calculate the current year
if choice.lower() == "yes":
    birth_year = int(input("Enter your birth year: "))
    current_year = birth_year+age
else:
    current_year = 2024

# Personalized greeting
print(f"Hello, {name}! You are {age} years old and it is the year {current_year}")

# Calculate the number of years
