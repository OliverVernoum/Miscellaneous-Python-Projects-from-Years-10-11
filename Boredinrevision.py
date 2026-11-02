for i in range(1,11):
    high_score = 0
    score = int(input("Enter your score: "))
    if score > high_score:
        high_score = score
        print("New high score!")

print(f"Your high score is: {high_score}")


