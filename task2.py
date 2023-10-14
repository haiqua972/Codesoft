import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Cannot calculate the square root of a negative number"
    else:
        return math.sqrt(x)
system= True
while True:
    try:
        num1 = eval(input("Enter the first number: "))
        operation = input("Enter an operation:\n + to Add\n - to Subtract\n * to Multiply\n / to divide\n ^ for power\n sqrt for square root\n e to Exit\n")

        if operation in ['+', '-', '*', '/', '^', 'sqrt']:
            if operation != 'sqrt':
                num2 = float(input("Enter the second number: "))    
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            elif operation == '^':
                result = power(num1, num2)
            elif operation == 'sqrt':
                result = square_root(num1)

            print(f"Result: {result}")
        elif operation =='e':
            break
        else:
            print("Invalid operation. Please enter +, -, *, /, ^, or sqrt.")
            continue
        
        another = input("Do you want to perform another calculation? (yes/no): ")
        if another.lower() != 'yes':
            break
    except Exception as e:
        print(f"An error occurred: {e}")

print("Exiting....")
        
