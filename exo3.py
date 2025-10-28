# Validation d'un age pour l'inscription
from colorama import Fore, Style

while True:
    try:
        age = int(input("Entrer Votre age ici: "))
    except ValueError:
        print("ERREUR: Veulliez entrer un entier")
        continue

    if age:
        if age < 18 :
            print(Fore.RED,"\nInscription Refuser",Style.RESET_ALL)
            continue

        elif age > 18:
            print(Fore.GREEN,"\nInscription Valider\n", Style.RESET_ALL)
            break
        


