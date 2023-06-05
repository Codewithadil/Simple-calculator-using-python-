# How to create a calulator using python

def add (a,b):
      # This function is used for adding two numbers  
    return a+b
def subtract (a,b):
    # This function is used for subtracting two numbers   
    return a-b
def multiply (a,b):
    # This function is used for multiplying two numbers 
    return a*b
def divide (a,b):
     # This function is used for dividing two numbers  
    return a/b
def floor_division(a,b):
     # This function is used for floor division  
    return a//b

print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. FLOOR DIVISION")

operation = input("Please enter given the above options: ")

num1 = int(input("Please Enter first no. "))
num2 = int(input("Please Enter second no. "))

if operation == "1":
    print(num1, "+", num2, "=", add(num1,num2), "Ans")
elif operation == "2":
    print(num1, "-", num2, "=", subtract(num1,num2), "Ans")
elif operation == "3":
    print(num1, "*", num2, "=", multiply(num1,num2), "Ans")
elif operation == "4":
    print(num1, "/", num2, "=", divide(num1,num2), "Ans")
elif operation == "5":
    print(num1, "//", num2, "=", floor_division(num1,num2), "Ans")
else:
    print("invalid input")

 # hello my name is adil alam
 
