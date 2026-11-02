complete = False
#Welcomes users to the calculator
print("Welcome to the calculator.")

num1=int(input("Please input your first number: "))

operation=input("Please enter your operation. Press 1 for Add, 2 for Subtract, 3 for Divide,4 for Multiply or 5 for Power. ")

num2=int(input("Please input your second number: "))


#Defines the operations such as Addition or Subtraction
def Addition(num1, num2):
    Add = num1 + num2
    print(int(Add))
   
def Subtraction(num1, num2):
    Min = num1 - num2
    print(int(Min))


def Multiplication(num1, num2):
    Times = num1*num2
    print(int(Times))

def Division(num1, num2):
    Div = num1 / num2
    print(int(Div))

def Power(num1, num2):
    Pow = num1**num2
    print(int(Pow))
    
#Checks decision of operation based on available functions   
while complete != True:
    
    if operation==("1"):
        Addition(num1,num2)
        complete = True


    elif operation==("2"):
        Subtraction(num1,num2)
        complete = True


    elif operation==("3"):
        Division(num1,num2)
        complete = True



    elif operation==("4"):
        Multiplication(num1,num2)
        complete = True


    elif operation==("5"):
        Power(num1,num2)
        complete = True


    else:
        print("Invalid")
