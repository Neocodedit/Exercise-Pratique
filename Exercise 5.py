# INFORMATION
#
#   Title: Practice Exercise #5 - 'Defining Functions'
#   Version: 1.00
#   Author: neocodedit
#   Created: 2025-05-24
#
#
# DESCRIPTION
#
#   Exercise(s)
#
#   1 - Rewrite the area2.py program from the Examples below to have a
#   separate function for the area of a square, the area of a rectangle,
#   and the area of a circle (3.14 * radius**2).
#   This program should include a menu interface.
#
#       Your Name: Josh
#       Hello!
#       Welcome, Josh
#
#       To find the area of a rectangle,
#       enter the width and height below.
#
#       Width: -4
#       Must be a positive number
#       Width: 4
#       Height: 3
#       Width = 4  Height = 3  so Area = 12
#
#
# UPDATES INDEX
#
#   (2025-05-24)(1.00): Program creation.

  
def input_validation(n):
    number = float(input(n))
    while number <= 0:
        print('✘ value must be bigger than 0.')
        print()
        number = float(input(n))
    return number

def square_area():
    height = input_validation('Height: ')
    print('Area: ', (height * height))

def rectangle_area():
    height = input_validation('Height: ')
    lenght = input_validation('lenght: ')
    print('Area: ', (height * lenght))

def circle_area():
    radius = input_validation('Radius: ')
    print('Area: ', (3.14 * radius**2))



choice = 4
name = input('Your name: ')
print('Welcome to Defining Functions 1.00,',name)
print('This program will calculate the area of a square, rectangle or circle.')

while choice != 0:
    print()
    print('[0] Exit')
    print('[1] Square')
    print('[2] Rectangle')
    print('[3] Circle')
    print()
    choice = int(input())
    print()
    if choice == 1:
        square_area()
    elif choice == 2:
        rectangle_area()
    elif choice == 3:
        circle_area()
    elif choice == 0:
        print('Bye!')
        break
    else:
        print('✘ must choose one of the options.')

        
print()
print('✔ Program successful.')
