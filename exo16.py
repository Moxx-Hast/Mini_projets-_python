# Prediction de meteo
from random import *
from colorama import *

t = randint(0,100)
h = randint(0,100)

if t > 25 and h > 60 :
    print(Fore.RED,"\nTemps chaud et humide\n",Style.RESET_ALL)

elif t < 15 and h > 70 :
    print(Fore.BLUE,"\nTemps froid et humide\n",Style.RESET_ALL)

else :
    print(Fore.MAGENTA,"\nTemps Normal\n",Style.RESET_ALL)


