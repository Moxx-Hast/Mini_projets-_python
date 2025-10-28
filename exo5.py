# Verification de Niveau d'un Mot de Passe
from colorama import Fore,Style

print("\n===== Verificateur du niveau de securiter d'un mot de passe =====")


while True:
    password = input("\nEntrer votre mot de passe: ")

    pass_len = len(password)

    if pass_len < 6 :
        print(Fore.RED,"\nMot de Passe Faible",Style.RESET_ALL)
        continue

    elif 6 <= pass_len <= 10 :
        print(Fore.YELLOW,"\nMots de Passe Moyen",Style.RESET_ALL)
        continue

    elif pass_len > 10 :
        print(Fore.GREEN,"\nMots de Passe Fort",Style.RESET_ALL)
        break





