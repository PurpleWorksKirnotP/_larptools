# Modules
import random
import os
import sys
import time

try:
    import colorama
    import requests
except:
    os._exit

from colorama import Fore, Back, Style
colorama.init(autoreset=True)


import ctypes

# Administ funcs

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )

if not is_admin():
    run_as_admin()
    sys.exit()
else:
    print(Fore.MAGENTA + Style.DIM + f"[DEBUG]: running as administrator")

# Initialization

r = requests.get("https://raw.githubusercontent.com/PurpleWorksKirnotP/_larptools/refs/heads/main/CustomizableTool/version.custotool")
ver = r.content

tn = "---[PHT]: "

print(Fore.MAGENTA + f"{tn} Welcome to custotool! version: {ver}")

username = input(Fore.GREEN + Style.BRIGHT + f"{tn} enter username: ").lower()
devicename = input(Fore.GREEN + Style.BRIGHT + f"{tn} enter device name: ").lower()

tn = f"---[PHT | {username}@{devicename}]: "

for i in range(1, random.randint(10,99999)):
    print(f"{tn} LOADING... UNPACKED {random.randint(1000,9999)}{random.choice([".txt",".dll",".exe"])} FROM {random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}")

print(f"{tn} Awaiting Command...")

# Actual Code
Yeslow = True
while Yeslow:
    inp = input(f"{tn} ").lower()
    bdy = inp.split()
    flag = bdy[0].lower()

    context = bdy[1].lower() if len(bdy) > 1 else "ERR: MISSING VAR"
    context2 = bdy[2].lower() if len(bdy) > 2 else "ERR: MISSING VAR"
    context3 = bdy[3].lower() if len(bdy) > 3 else "ERR: MISSING VAR"

    if flag == "h":
        print("insert help")
    elif flag in ["exit", "-e", "e"]:
        print(f"{tn} exitting... goodbye {username}")
        time.sleep(2)
        break
    else:
        print(f"{tn} What did you even put???")