# Write a python script that generates an acronym word from given sentence.

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

user_input = input(Back.LIGHTMAGENTA_EX+Fore.LIGHTBLACK_EX+"Enter a sentence: ")
list = user_input.split()
print(Back.GREEN + Fore.MAGENTA + "List:" + str(list))
acr = ""
for i in list:
    acr = acr+str(i[0])
print(Back.RED + Fore.BLUE +"Acronym for the sentence:" + acr.upper())
