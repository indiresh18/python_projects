print("we are going to build an calculator")
print("===============SIMPLE CALCULATOR===============")
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error: division by zero"
    else:
        return x/y
while(1):
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply") 
    print("4.Divide")
    print("5.Exit")
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice=='1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "+", num2, "=", add(num1,num2))
    elif choice=='2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "-", num2, "=", subtract(num1,num2))
    elif choice=='3'   :
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "*", num2, "=", multiply(num1,num2))
    elif choice=='4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "/", num2, "=", divide(num1,num2))
    elif choice=='5':
        print("Exiting the calculator. Goodbye!")
        break         
    else:
        print("Invalid Input")
                
    