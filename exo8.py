# Temperature du capteur
from colorama import Fore,Style

while True: 
    try:
        temperature = int(input("\nQuelle est la temperature de la piece? "))
    except ValueError:
        print("\nERREUR: Veulliez entrer la temperature en °C")
        continue

    if 20 <= temperature <= 30:
        print(Fore.GREEN,"\nTemperature Normal\n",Style.RESET_ALL)
        break

    elif temperature < 20 :
        print(Fore.BLUE,"\nTemperature Basse\n",Style.RESET_ALL)
        break

    else :
        print(Fore.RED,"\nSurchauffe\n",Style.RESET_ALL)
        break
        
