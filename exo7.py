# analyse du niveau d'alerte
from colorama import Fore,Style

niveau_alerte = int(input("\nEntrer le niveau d'alerte: "))

match niveau_alerte:
    
    case 1 :
        print(Fore.GREEN,"\nNiveau d'alerte Faible\n",Style.RESET_ALL)

    case 2 :
        print(Fore.BLUE,"Niveau d'alerte Modérée\n",Style.RESET_ALL)

    case 3 :
        print(Fore.CYAN,"Niveau d'alerte élevée\n",Style.RESET_ALL)

    case 4 :
        print(Fore.MAGENTA,"Niveau d'alerte Critique\n",Style.RESET_ALL)

    case 5 :
        print(Fore.YELLOW,"Niveau d'alerte Maximal\n",Style.RESET_ALL)

    case _:
        print(Fore.RED,"Niveau d'alerte inconnu\n",Style.RESET_ALL)




