temp_value = float(input('Enter the temperature value: '))
temp_unit = input('Enter the unit (Celsius, Fahrenheit, Kelvin): ')

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)  
    return celsius_to_fahrenheit(celsius)
def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

print('Enter 1: Convert Fahrenheit to Celsius')
print('Enter 2: Convert Celsius to Fahrenheit')
print('Enter 3: Convert Celsius to Kelvin')
print('Enter 4: Convert Kelvin to Fahrenheit')
print('Enter 5: Convert Fahrenheit to Kelvin')

user_input = int(input('Enter a number of conversion: '))
if user_input == 1 and temp_unit == 'Fahrenheit':
    print(fahrenheit_to_celsius(temp_value))
elif user_input == 2 and temp_unit == 'Celsius':
    print(celsius_to_fahrenheit(temp_value))
elif user_input == 3 and temp_unit == 'Celsius':
    print(celsius_to_kelvin(temp_value))
elif user_input == 4 and temp_unit == 'Kelvin':  
    print(kelvin_to_fahrenheit(temp_value))
elif user_input == 5 and temp_unit == 'Fahrenheit':  
    print(fahrenheit_to_kelvin(temp_value))