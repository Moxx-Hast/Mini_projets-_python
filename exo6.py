# decision d'investissement selon le taux de rentabiliter
from colorama import Fore,Style

while True:
    try:
        tdr = int(input("\nEntrer le taux de rentabiliter ici svp: "))
    except ValueError:
        print("\nERREUR: Vous devez entrer le taux de rentabiliter en pourcentage (%)")
        continue

    if tdr < 5 :
        print(Fore.RED,"\nProjet non Rentable\n",Style.RESET_ALL)
        break

    elif 5 <= tdr <= 10 :
        print(Fore.YELLOW,"\nProjet a Risque\n", Style.RESET_ALL)
        break

    elif tdr > 10 :
        print(Fore.GREEN,"\nProjet Rentable\n", Style.RESET_ALL)
        break




