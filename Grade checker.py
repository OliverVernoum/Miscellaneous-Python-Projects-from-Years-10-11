#This welcomes users to the program
print("Welcome to the Grade Determiner")
#Ths makes variables and allows the user to enter their score
grade1=float(input("Please enter your first score in percentage: "))

grade2=float(input("Please enter your second score in percentage: "))

#This determines the average
avg=(grade1+grade2)/2

#This determines a grade based on the average and displays their average and their grade to the user

if avg==0:
    print("You got a U. This is because you scored",avg,"")

elif avg<=10:
    print("You got an F- or a 1  This is because you scored",avg,"")

elif avg<=20:
    print("You got an F or a 2 This is because you scored",avg,"")

elif avg<=30:
    print("You got a D or a 3 This is because you scored",avg,"")

elif avg<=40:
    print("You got a C or a 4 This is because you scored",avg,"")

elif avg<=60:
    print("You got a C+ or a 5 This is because you scored",avg,"")

elif avg<=70:
    print("You got a B or a 6  This is because you scored",avg,"")

elif avg<=80:
    print("You got a B+ or a 7 This is because you scored",avg,"")

elif avg<=90:
    print("You got an A or an 8 This is because you scored",avg,"")

elif avg<=95:
    print("You got an A* or a 9 This is because you scored",avg,"")

elif avg<=100:
    print("You got an A* or a 9. Full marks! This is because you scored",avg,"")

else:
    print("Invalid. Please try again.")



