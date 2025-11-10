###
# A program that prints your height both in cm and in feet and inches.
#
cm = input('Enter your height in cm: ')
feet = float(cm) / 30.48
inches = float(cm) / 2.54

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')