# Detection de Niveau d'energie
from random import *
from colorama import Fore,Style

batterie = randint(0,100)

if batterie >= 80 :
    print(Fore.GREEN,"Energie Suffisante!",Style.RESET_ALL)

elif batterie >= 40 :
    print(Fore.YELLOW,"Energie Moyenne!",Style.RESET_ALL)

else :
    print(Fore.RED,"Energie Faible!",Style.RESET_ALL)

