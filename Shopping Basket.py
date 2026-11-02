price_apples = 0.50
price_bread = 1.20
price_milk = 0.80

money = float(input("Enter the amount of money you have: "))


num_apples_bought = int(input("How many apples do you want to buy? "))
num_bread_bought = int(input("How many loaves of bread do you want to buy? "))
num_milk_bought = int(input("How many bottles of milk do you want to buy? "))

total_apples = num_apples_bought * price_apples
total_bread = num_bread_bought * price_bread
total_milk = num_milk_bought * price_milk

total_cost = total_apples + total_bread + total_milk
if total_cost > money:
    print("You do not have enough money to buy these items.")
else:
    print("skib")