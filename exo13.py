# choix du mode d'apprentissage
from colorama import *

print("\n===== Bienvenue dans votre choix d'apprentissage =====\n")
print("1 -Apprentissage Supervisser")
print("2 -Apprentissage non Supervisser")
print("3 -Apprentissage par renforcement")


list_choix = [1,2,3]

while True:
    try:
        choix = int(input("\nFaite Votre choix ici: "))
    except ValueError:
        print(Fore.RED,"\nErreur",Style.RESET_ALL)
        continue

    if choix  in list_choix:
        match choix:
            case 1:
                print("\nVous avez choissie de faire un ",Fore.BLUE,"Apprentissage Supervisser\n",Style.RESET_ALL)

            case 2:
                print("\nVous avez choissie de faire un ",Fore.BLUE,"Apprentissage non Supervisser\n",Style.RESET_ALL)

            case 3:
                print("\nVous avez choissie de faire un ",Fore.BLUE,"Apprentissage par renforcement\n",Style.RESET_ALL)

        break

    else:
        print(Fore.RED,"\nChoisit un chiffre entre 1 et 3",Style.RESET_ALL)
        continue