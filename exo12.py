# Diagnostic intelligent
from colorama import Fore,Style

while True:
    print("\n===== Bienvenue dans le Diagnoatic intelligent =====")

    print("Veulliez saisir:",Fore.RED," 0(pour non) ",Style.RESET_ALL,"et",Fore.GREEN," 1(pour oui)",Style.RESET_ALL)

    try:
        fievre = int(input("\nAvez-vous de la fievre?: "))
        toux = int(input("\nAvez-vous de la Toux?: "))
        fatigue = int(input("\nEtes vous fatiguer?: "))
    except ValueError:
        print("\nERREUR: Veulliez entrer soit:",Fore.RED," 0(NON)",Style.RESET_ALL,"OU",Fore.GREEN," 1(OUI)",Style.RESET_ALL)
        continue
    
    if fievre == 1 and toux == 1 and fatigue == 1 :
        print(Fore.RED,"\nRisque élevée!",Style.RESET_ALL)

        
    elif toux == 1 and fatigue == 1 or fievre == 1 and toux == 1 or fievre == 1 and fatigue == 1 :
        print(Fore.YELLOW,"\nRisque Modéré",Style.RESET_ALL)

    elif toux == 1 or fatigue == 1 or fievre == 1 :
        print(Fore.BLUE,"\nRisque Faible",Style.RESET_ALL)
    
    else:
        print(Fore.GREEN,"\nAucun Risque pour vous",Style.RESET_ALL)

    try :
        fini = int(input("\nEn etes Vous Sur?: "))
    except ValueError:
        print("\nEntrer 1 OU 0")
        continue

    if fini == 1 :
        print(Fore.MAGENTA,"\nD'accord, Bon traitement a vous!",Style.RESET_ALL)
        break

    else :
        print("\nDac, recommencons")
        continue






