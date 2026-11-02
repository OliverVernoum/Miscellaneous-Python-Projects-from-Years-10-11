base_price= 8.00

age = int(input("Please enter your age: "))

if age < 12:
    price = base_price * 0.5
    print(f"Your ticket price is £{price:.2f}")

elif age >= 65:
    price = base_price * 0.75
    print(f"Your ticket price is £{price:.2f}")

else:
    price = base_price
    print(f"Your ticket price is £{price:.2f}")