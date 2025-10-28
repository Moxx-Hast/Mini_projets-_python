# Reconnaissance vocal simple
from colorama import Fore,Style


while True:
    print("\nveulliez entree une lettre(en grand caractere) pour executer une commande(B,pour arreter le programme)")
    Vocal = input("\nEntrer une lettre: ").title()

    if Vocal == "A" :
        print(Fore.BLUE,"\nAllumer la lumiere",Style.RESET_ALL)
        continue

    elif Vocal == "E" :
        print(Fore.CYAN,"\nEteindre la lumiere",Style.RESET_ALL)
        continue

    elif Vocal == "R" :
        print(Fore.MAGENTA,"\nRedemarer le systeme",Style.RESET_ALL)
        continue

    elif Vocal == "B" :
        print(Fore.RED,"\nArret du Systeme\n",Style.RESET_ALL)
        break

    else :
        print("\nVous-Vous etes tromper!🤣, tu peut toujour recommencer",Style.RESET_ALL)
        continue


