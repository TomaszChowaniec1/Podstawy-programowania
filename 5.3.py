###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
length = int(a)
width = int(b)
height = int(c)
volume = length * width * height
surface = 2 * (length *width + length * height + width * height)
print(f'The volume of the cuboid is {volume} and surface is {surface}')