# Verification de mot de passe
from colorama import Fore,Style

correct_password = "Cyber@2025"
while True:
    user_password = input("\nEntrer le mot de passe correct pour vous connecter: ")

    if user_password == correct_password :
        print(Fore.GREEN, "\nAcces Autorisser", Style.RESET_ALL)
        break

    else :
        print(Fore.RED,"\nAcces Refusser\n", Style.RESET_ALL)
        continue

