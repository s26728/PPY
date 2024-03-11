# Prompt the user to enter their name
name = input("Enter your name: ")
# Print a personalized greeting message
print("Hello,", name + "!")

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
print("Hello,", name, surname, "of age", age + "!")

celsius = float(input("Enter temperature in Celsius: "))
# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32
# Print the converted temperature
print("Temperature in Fahrenheit:", fahrenheit)
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = 5/9 * (fahrenheit - 32)
# Print the converted temperature
print("Temperature in Celsius:", celsius)
# Define variable
score = float(input("Enter your score: "))

# Determine the grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
# Print the grade
print("Your grade is:", grade)

# Define variable
score = float(input("Enter your score: "))
# Determine the grade
if score >= 98:
    grade = "6"
elif score >= 90:
    grade = "5"
elif score >= 75:
    grade = "4"
elif score >= 50:
    grade = "3"
else:
    grade = "2"
# Print the grade
print("Your grade is:", grade)

# Define variable
number = int(input("Enter a number: "))
# Check if the number is even or odd
if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"
# Print the result
print("The number is:", result)

# Define variable
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
# Check if the number is even or odd
if number1 % number2 == 0:
    result = "divisible"
else:
    result = "not divisible"
# Print the result
print("The number is", result, "by the second number.")

# Prompt the user to enter values of different types
var_int = int(input("Enter an integer value: "))
var_float = float(input("Enter a float value: "))
var_str = input("Enter a string value: ")
var_bool = input("Enter a boolean value (True or False): ").lower() == "true"
# Determine the type of each variable
type_int = type(var_int).__name__
type_float = type(var_float).__name__
type_str = type(var_str).__name__
type_bool = type(var_bool).__name__
# Print the type of each variable
print("Type of var_int:", type_int)
print("Type of var_float:", type_float)
print("Type of var_str:", type_str)
print("Type of var_bool:", type_bool)

# Define variables
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
# Check the type of triangle
if side1 == side2 == side3:
    triangle_type = "Equilateral"
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle_type = "Isosceles"
else:
    triangle_type = "Scalene"

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side3 + side2 > side1):
    triangle_check = "possible"
else:
    triangle_check = "not possible"
# Print the type of triangle
print("The triangle is:", triangle_type)
print("The triangle is", triangle_check, "to draw.")

# Define variables
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
# Perform the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Attempt to divide by zero"
    else:
        result = num1 / num2
else:
    result = "Invalid operation"
# Print the result
print("Result:", result)