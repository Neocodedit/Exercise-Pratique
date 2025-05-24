# INFORMATION
#
#   Title: Practice Exercise #4 - 'Decisions'
#   Version: 1.00
#   Author: neocodedit
#   Created: 2025-05-24
#
#
# DESCRIPTION
#
#   Exercise(s)
#
#   1 - Write a program that asks the user their name,
#   if they enter your name say "That is a nice name",
#   if they enter "John Cleese" or "Michael Palin",
#   tell them how you feel about them.
#   otherwise tell them "You have a nice name."
#
#   2 - Write a program that makes the user guess a number.
#   keep track of how many times the user has entered the wrong number.
#   If it is more than 3 times, print "That must have been complicated."
#   otherwise print "Good job!"
#
#   3 - Write a program that asks for two numbers.
#   If the sum of the numbers is greater than 100, print "That is a big number."
#
# UPDATES INDEX
#
#   (2025-05-24)(1.00): Program creation.



# BLOCK 1 - Name input.

name = input('Name: ')

if name == 'neocodedit':
    print('That is a nice name.')
elif name == 'Michael Palin' or 'John Cleese':
    print('Weird name, but okay.')
else:
    print('You have a nice name.')



# BLOCK 2 - Guess the number.

usernumber = 0
definednumber = 5
tryamount = 1

print()
print('Ok', name +', can you guess the correct number between 1-10?')

while usernumber != definednumber:
    usernumber = int(input())
    tryamount = tryamount + 1
    if usernumber > definednumber:
        print('✘ The number is smaller.')
    elif usernumber < definednumber:
        print('✘ The number is bigger.')
    
    
print('✔')
if tryamount <= 3:
    print('Good job.')
else:
    print('That must have been complicated.')



# BLOCK 3 - User numbers addition.


print()
print('Alright. Lets add up numbers', name)
number1 = int(input('First number: '))
number2 = int(input('Second number: '))
if number1 + number2 >= 100:
    print(number1, '+', number2,'=', (number1 + number2))
    print('That is a big number.')
else:
    print(number1, '+', number2, '=', (number1 + number2))
