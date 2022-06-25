import random, string, requests, webbrowser, time
import base64
import os
import random
import string
import requests
from colorama import *

f = open("Valid Nitro.txt", "w", encoding='utf-8')

print("""

 attention !! 
      Vous devez attendre environ 5 heures pour 1 code valide
      
     djrobin gen (Par djrobin)                              
                                                                    """)

while True:
    code = ('').join(random.choices(string.ascii_letters + string.digits,
                                    k=16))
    r = requests.get(
        f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    )
    if r.status_code == 200:
        print(Fore.GREEN + f"Gg le code du nitro est valide > https://discord.gift/{code}"
        )
        f.write(f"discord.gift/{code}\n")
    else:
        print(Fore.RED + f"Nitro Invalide > https://discord.gift/{code}")
