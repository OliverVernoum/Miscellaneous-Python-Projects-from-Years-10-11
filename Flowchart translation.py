

def mainloop():
    print("Hello, my name is Susan from Space.")
    name = input("What is your name? ")
    print(f"Hello {name}. I am from the year 2210 and I am 20 years old")
    age = int(input("How old are you? "))
    future_age = (age + (2210-2025))
    print(f"Wow, by 2210 you'll be {future_age}, that is really old!")
    music = input(f"What music are you into? ")
    print(f"I have not heard of {music}")


mainloop()
