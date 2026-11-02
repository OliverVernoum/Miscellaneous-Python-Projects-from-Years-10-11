import math 



num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))

def Addition(num1, num2):
    num3 = num1 + num2
    print(num3)

def Subtraction(num1,num2):
    num3 = num1 - num2
    print(num3)

def Multiplication(num1,num2):
    num3 = num1 * num2
    print(num3)

def Division(num1,num2):
    num3 = num1 / num2
    print(num3)

def Power(num1,num2):
    num3 = num1**num2
    print(num3)

def Remainder(num1,num2):
    num3 = num1 % num2
    num4 = num1 // num2
    print(f"{num4} remainder {num3}")

def Root(num1,num2):
    num3 = math.pow(num1, 1/num2)
    print(num3)

def Sine(num1):
    num3 = math.sin(math.degrees(num1))
    print(num3)

def Cosine(num1):
    num3 = math.cos(math.degrees(num1))
    print(num3)

def Tangent(num1):
    num3 = math.tan(math.degrees(num1))
    print(num3)


operation = input("Enter your operation. Press 1 for Add, 2 for Subtract, 3 for Divide, 4 for Multiply, 5 for Power, 6 to divide with remainder, 7 to put the first number to the root of the second number, or type sin cos and tan to get the respective function of the first number: ")

if operation == ("1"):
    Addition(num1,num2)

elif operation == ("2"):
    Subtraction(num1,num2)

elif operation == ("3"):
    Division(num1,num2)

elif operation == ("4"):
    Multiplication(num1,num2)

elif operation == ("5"):
    Power(num1,num2)

elif operation == ("6"):
    Remainder(num1,num2)

elif operation == ("7"):
    Root(num1,num2)
 
elif operation == ("sin"):
    Sine(num1)

elif operation == ("cos"):
    Cosine(num1)

elif operation == ("tan"):
    Tangent(num1)
