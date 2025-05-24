# INFORMATION
#
#   Title: Practice Exercise #3 - 'Count to 10'
#   Version: 1.01
#   Author: neocodedit
#   Created: 2025-05-24
#
#
# DESCRIPTION
#
#   Exercise(s)
#
#   1 - Write a program that asks the user for a Login Name and password.
#   Then when they type "lock", they need to type in their name and password
#   to unlock the program.
#
#
# UPDATES INDEX
#
#   (2025-05-24)(1.00): Program creation.
#   (2025-05-24)(1.01): Simplification of the code. Added a loop when
#   the user's input does not match 'username', 'password' or "lock".


username = input('Choose a username: ')
password = input('Define your password: ')
print()
print('Type in "lock" to confirm your new username & password.')

while input() != 'lock':
    print('✘')

while input('Confirm your username: ') != username or input('Confirm your password: ') != password:
    print('✘')


print()
print('✔ Program successful.')
