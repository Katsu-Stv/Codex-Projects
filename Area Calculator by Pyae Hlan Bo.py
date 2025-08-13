#Area Calculator

import math

#Shape Variables 
triangle = 0
rectangle = 0
square = 0
circle = 0

#Length Variables
base = 0
height = 0
length = 0
width = 0
side = 0
radius = 0

print('==================')
print('Area Calculator 📐')
print('==================')
print('\n')
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")
print('\n')

shape = int(input('Which shape: '))

if shape == 1:
    triangle += 1
elif shape == 2:
    rectangle += 1
elif shape == 3:
    square += 1
elif shape == 4:
    circle += 1
else:
    print('\n')
    print('You have quit.')

print('\n')

if triangle == 1:
    base = int(input('Base: '))
    height = int(input('Height: '))

    area = (base * height) / 2
elif rectangle == 1:
    length = int(input('Length: '))
    width = int(input('Width: '))

    area = length * width
elif square == 1:
    side = int(input('Side:'))

    area = side ** 2
else:
    radius = int(input('Radius:'))

    area = math.pi * (radius ** 2)

print('\n')
print(f"The area is {area}.")