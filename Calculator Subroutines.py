
#Welcomes users to the calculator
print("Welcome to the calculator.")

num1=float(input("Please input your first number: "))

operation=input("Please enter your operation. Press 1 for Add, 2 for Subtract, 3 for Divide,4 for Multiply or 5 for Power. ")

num2=float(input("Please input your second number: "))


#Defines the operations such as Addition or Subtraction
def Addition():
    print(num1+num2)

def Subtraction():
    print(num1-num2)

def Multiplication():
    print(num1*num2)

def Division():
    print(num1/num2)

def Power():
    print(num1**num2)
    

if operation==("1"):
    Addition()


elif operation==("2"):
    Subtraction()


elif operation==("3"):
    Division()



elif operation==("4"):
    Multiplication()


elif operation==("5"):
    Power()


else:
    print("Invalid")
