# Python Program for Program to find area of a circle
import math


def area_of_circle(r):
    return 0 if r <= 0 else math.pi * r**2


radius = int(input('Enter the radius of the circle: '))
print(f'The area of {radius} is {round(area_of_circle(radius),2)}')

