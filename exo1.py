# saisi et affichage du nom d'un etudiant
from colorama import Fore, Style, Back

while True:
    name = input("\nEntrer votre nom: ").title().strip()
    if name:
        print("\nvotre nom est donc:", Fore.BLUE, name, Style.RESET_ALL)
        break
        
    else:
        print(Fore.RED,"Vous devez entrer votre nom",Style.RESET_ALL)
        continue
    



