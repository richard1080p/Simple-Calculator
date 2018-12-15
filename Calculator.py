#This is a simple calculator that can carry out simple functions like addition,
#subtraction, multiplication, division

#This is for addition
def add(x, y):
    return x + y

#This is for subtraction
def subtract(x, y):
    return x - y

#This is for multiplication
def multiply(x, y):
    return x * y

#This is for division
def divide(x, y):
    return x / y

print ("Select an operation.")
print ("1.Add")
print ("2.Subtract")
print ("3.multiply")
print ("4.Divide")

#This is to take input from the user
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter The First Number: "))
num2 = int(input("Enter The Second Number: "))

if choice == '1':
    print(num1,"+",num2, "=", add(num1,num2))
elif choice == '2':
    print (num1,"-",num2, "=", subtract(num1,num2))
elif choice == '3':
    print (num1,"*",num2, "=", multiply(num1,num2))
elif choice == '2':
    print (num1,"/",num2, "=", divide(num1,num2))
else:
    print("Invalid input")

