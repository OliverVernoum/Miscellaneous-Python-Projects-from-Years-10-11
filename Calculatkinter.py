import tkinter as tk

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
    
   
if operation==("1"):
    Addition(num1,num2)


elif operation==("2"):
    Subtraction(num1,num2)


elif operation==("3"):
    Division(num1,num2)



elif operation==("4"):
    Multiplication(num1,num2)


elif operation==("5"):
    Power(num1,num2)

    tk.Button(root, text="Add", command=lambda: operation_var.set("1")).grid(row=5, column=0)
    tk.Button(root, text="Subtract", command=lambda: operation_var.set("2")).grid(row=5, column=1)
    tk.Button(root, text="Multiply", command=lambda: operation_var.set("4")).grid(row=6, column=0)
    tk.Button(root, text="Divide", command=lambda: operation_var.set("3")).grid(row=6, column=1)
else:
    print("Invalid")
    def calculate():
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        operation = operation_var.get()
        
        if operation == "1":
            result = num1 + num2
        elif operation == "2":
            result = num1 - num2
        elif operation == "3":
            result = num1 / num2
        elif operation == "4":
            result = num1 * num2
        elif operation == "5":
            result = num1 ** num2
        else:
            result = "Invalid operation"
        
        result_label.config(text="Result: " + str(result))

    root = tk.Tk()
    root.title("Calculator")

    tk.Label(root, text="First Number:").grid(row=0, column=0)
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1)

    tk.Label(root, text="Second Number:").grid(row=1, column=0)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1)

    tk.Label(root, text="Operation:").grid(row=2, column=0)
    operation_var = tk.StringVar()
    operation_var.set("1")
    tk.OptionMenu(root, operation_var, "1", "2", "3", "4", "5").grid(row=2, column=1)

    tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

    result_label = tk.Label(root, text="Result: ")
    result_label.grid(row=4, column=0, columnspan=2)

    root.mainloop()