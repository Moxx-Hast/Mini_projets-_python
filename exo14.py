# Controle d'acces celon le role
from colorama import *


while True:
    print("\n===== Programme de Controle d'acces =====")

    grade = input("\nQuelle est votre Grade?: ")

    if grade == "admin":
        print("\nvous etes donc grade",Fore.RED," Admin",Style.RESET_ALL)
        print(Fore.GREEN,"Acces total\n",Style.RESET_ALL)
        break

    elif grade == "utilisateur":
        print("\nvous etes donc grade",Fore.YELLOW," utilisateur",Style.RESET_ALL)
        print(Fore.MAGENTA,"Acces Restreint\n",Style.RESET_ALL)
        break

    elif grade == "inviter":
        print("\nvous etes donc grade",Fore.CYAN," inviter",Style.RESET_ALL)
        print(Fore.RED,"Acces limité\n",Style.RESET_ALL)
        break

    else :
        print(Fore.RED,"\nCe Grade n'exixte pas",Style.RESET_ALL)
        continue


