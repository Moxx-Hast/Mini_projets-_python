# Somme et Moyenne de 2 Nombre
from colorama import Fore,Style

while True :
    try:
        a = int(input("\nEntrer une premiere valeur: "))
        b = int(input("\nEntrer une deuxieme valeur: "))
    except ValueError:
        print(Fore.RED,"\nVeuilliez entrer une valeur numerique!!!",Style.RESET_ALL)
        continue

    if a != 0 and b !=0 :
        som = a+b
        print("\nLa Somme de", a, "+", b, "=", som)
        moy = som/2
        print("\nleurs moyenne est ", moy)
        break




