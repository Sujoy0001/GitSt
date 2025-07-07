# 1. Define add function
def add(x, y):
    return x + y

# 2. Define subtract function
def subtract(x, y):
    return x - y

# 3. Define multiply function
def multiply(x, y):
    return x * y

# 4. Define divide function
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# 5. Main code
print("Select operation:")
print("1.Add 2.Subtract 3.Multiply 4.Divide")

choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if choice == '1':
    print(add(num1, num2))
elif choice == '2':
    print(subtract(num1, num2))
elif choice == '3':
    print(multiply(num1, num2))
elif choice == '4':
    print(divide(num1, num2))
else:
    print("Invalid input")
