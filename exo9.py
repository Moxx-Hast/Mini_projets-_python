# Decision du mouvement d'un robot
from colorama import Fore,Style

while True:
    try:
        signal = float(input("\nEntrer le signal de proximiter(en cm): "))
    except ValueError:
        print("\nERREUR: Entrer une valeur reel")
        continue

    if signal > 50 :
        print("\nLe Robot",Fore.GREEN, "Avance!", Style.RESET_ALL)
        continue

    elif 20 <= signal <= 50:
        print("\nLe Robot",Fore.YELLOW, "Ralenti!", Style.RESET_ALL)
        continue

    else :
        print("\nLe Robot",Fore.RED, "S'arrete!\n", Style.RESET_ALL)
        break


