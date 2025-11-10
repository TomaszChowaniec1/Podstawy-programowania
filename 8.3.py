###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
celsius = input('Enter temperature in Celsius: ')
fahrenheit = (float(celsius) * 9/5) + 32
kelvin = float(celsius) + 273.15
print(f'Temperature in Fahrenheit: {fahrenheit}')
print(f'Temperature in Kelvin: {kelvin}')
