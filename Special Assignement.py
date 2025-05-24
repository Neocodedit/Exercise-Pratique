# INFORMATION
#   Special Assignement
#   Version: 1.1.0
#   Auteur: neocodedit
#   Date de Creation: 2025-05-20
# 
# INDEX DE UPDATES
#   1.0.0 Creation
#   1.0.1 Update: Print une liste de 'n' chiffres.
#   1.0.2 Update: Ajout de 'm1' et 'm2'.
#   1.0.3 Update: Ajout de l'addition de 'm1' et 'm2'.
#   1.0.4 Update: Simplification du code.
#   1.0.5 Update: Print seulement les multiples de 'm1' et 'm2'.
#   1.0.6 Update: Ajout d'un index de variables.
#   1.0.7 Update: Renommer variables.
#   1.0.8 Update: Fix dans les 'print'. Input pour 'm1' et 'm2'.
#   1.0.9 Update: Retour de lequation.
#   1.1.0 Update: Regroupement des resultats de 'm1', 'm2' et de 'm1' & 'm2'.
# 
# INDEX DE VARIABLES
#   i : Index
#   n : Le nombre de chiffre total a imprimer.
#   m1 : Valeur du premier multiple a trouver.
#   m2 : valeur du deuxieme multiple a trouver.
#   x : Modulo Operator de 'i' et 'm1'.
#   y : Modulo Operator de 'i' et 'm2'.

n = int(input('Chiffres de 0 - '))
m1 = int(input('Trouver les multiples de '))
m2 = int(input('et de '))

print()
print('Multiples de', m1)
i = 0
while i < n:
    i = i + 1
    x = i % m1
    if x == 0:
        print(i,'(',m1,'x',int(i/m1),')')
print()
print('Multiples de', m2)
i = 0
while i < n:
    i = i + 1
    y = i % m2
    if y == 0:
        print(i,'(',m2,'x',int(i/m2),')')
print()
print('Multiples de ',m1,' et ',m2)
i = 0
while i < n:
    i = i + 1
    x = i % m1
    y = i % m2
    if y == 0 and x == 0:
        print(i,'(',m1,'x',int(i/m1),')',' ou ','(',m2,'x',int(i/m2),')')

