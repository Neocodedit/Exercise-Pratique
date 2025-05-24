# INFORMATION
#
#   Title: Practice Exercise #3 - 'Count to 10'
#   Version: 1.02
#   Author: neocodedit
#   Created: 2025-05-24
#
#
# DESCRIPTION
#
#   Exercises
#   1 - Write a program that asks the user for a Login Name and password.
#   Then when they type "lock", they need to type in their name and password
#   to unlock the program.
#
#
# UPDATES INDEX
#
#   (2025-05-24)(1.00): Program creation.
#   (2025-05-24)(1.01): Simplification of the code. Added a loop when
#   the user enters the wrong username, password or "lock".


username = input('Choose a username: ')
password = input('Define your password: ')
print()
print('Type in "lock" to confirm your new username & password.')

while input() != 'lock':
    print('✘')

print('✔ Program locked.')

while input('Confirm your username: ') != username or input('Confirm your password: ') != password:
    print('✘')

print('✔ Program unlocked.')
print('Welcome to Exercise #3 (1.00)')
