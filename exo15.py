# Capteur de Luminisité
from random import randint
from colorama import *

lum = randint(0,100)


if lum < 30 :
    print(Fore.GREEN,"\nAllumer les lumieres",Style.RESET_ALL)

elif lum <= 70 :
    print(Fore.YELLOW,"\nMode Automatique",Style.RESET_ALL)

elif lum > 70 :
    print(Fore.RED,"\nEteindre les lumieres",Style.RESET_ALL)



    


