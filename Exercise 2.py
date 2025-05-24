# INFORMATION
#
#   Title: Practice Exercise #2 - 'Who goes there?'
#   Version: 1.00
#   Author: neocodedit
#   Created: 2025-05-24
#
#
# DESCRIPTION
#
#   Exercise(s)
#
#   1 - Write a program that gets 2 string variables
#   and 2 number variables from the user.
#   concatenates (joins them together with no spaces)
#   and displays the strings, then multiplies the two numbers on a new line.
#
#
# UPDATES INDEX
#
#   (2025-05-24)(1.00): Program creation.


string1 = str(input('First word: '))
string2 = str(input('Second word: '))
number1 = int(input('First number: '))
number2 = int(input('Second number: '))

print()
print(string1 + string2)
print(number1,'x',number2,'=',(number1 * number2))


print()
print('✔ Program successful.')
