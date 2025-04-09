print('Select an operation: ')
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Quit")

user_input = int(input('Please enter your choice:'))

if user_input == 1:
    num1 = float(input('Enter first number to add: '))
    num2 = float(input('Enter second number to add: '))
    result = num1 + num2
    print(f'{num1} + {num2} is {result}')
elif user_input ==2:
    num1 = float(input('Enter first number to subtract: '))
    num2 = float(input('Enter second number to subtract: '))
    result = num1 - num2
    print(f'{num1} - {num2} is {result}')
elif user_input == 3:
    num1 = float(input('Enter first number to multiply: '))
    num2 = float(input('Enter second number to multiply: '))
    result = num1 * num2
    print(f'{num1} * {num2} is {result}')
elif user_input == 4:
    num1 = float(input('Enter first number to divide: '))
    num2 = float(input('Enter second number to divide: '))
    if num2 == 0:
        print('Cannot divide by zero!')
    else:
        result = num1 / num2
        print(f'{num1} / {num2} is {result}')
elif user_input == 5:
    print('You chose to quit, Goodbye! ')
    exit()
else:
    print('That is not a valid choice')