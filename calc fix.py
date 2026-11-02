print("Welcome to the calculator.")

num1=float(input("Please input your first number: "))

operation=input("Please enter your operation. Press 1 for Add, 2 for Subtract, 3 for Divide,4 for Multiply or 5 for Power. ")

num2=float(input("Please input your second number: "))

numplus=num1+num2
nummin=num1-num2
numdiv=num1/num2
nummul=num1*num2
numpow=num1**num2

if operation==("1"):
    print(numplus)


elif operation==("2"):
    print(nummin)


elif operation==("3"):
    print(numdiv)



elif operation==("4"):
    print(nummul)


elif operation==("5"):
    print(numpow)


else:
    print("Invalid")
