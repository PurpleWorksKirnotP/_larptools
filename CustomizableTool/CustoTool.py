import random
import os
try:
    import colorama
    import requests
except:
    os._exit


from colorama import Fore, Back, Style
colorama.init(autoreset=True)

r = requests.get("https://1.1.1.1")
ver = r.content

ptn = "---[CUSTOTOOLINSTALL]: "
tn = ""

print(Fore.MAGENTA + f"{ptn} Welcome to custotool! version: {ver}")

newtoolname = input(Fore.GREEN + Style.BRIGHT + f"{ptn} input new toolname: ").strip().lower()