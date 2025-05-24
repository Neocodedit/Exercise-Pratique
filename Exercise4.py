# INFORMATION
#   EXERCISE PRATIQUE 4 'Trouver le bon numero'
#   Version: 1.0.1
#   Auteur: neocodedit
#   Date de Creation: 2025-05-22
#
# INDEX DE UPDATES
#   1.0.0 Update: Creation du code de base.
#   1.0.1 Update: Ajout du compte dessaie avant de trouver la solution.
#
# INDEX DE VARIABLES
#   n : Le chiffre a trouver.
#   x : Le chiffre choisi par l'utilisateur.
#   y : nombre d'essaies total avant de trouver la solution.
#
# INDEX DE FONCTIONS


n = 3
x = 0
y = 0

print('Trouves le bon numero.')

while x != n:
    x = int(input())
    y = y + 1
    if x > n:
        print('plus petit.')
    elif x < n:
        print('plus grand.')
    else:
        if y > 3:
            print('That must have been complicated.')
        elif y <= 3:
            print('Good job.')
 
