
import requests
from rich.console import Console
from time import sleep
from colorama import Fore

#LogProgress

console = Console()

def criar_arquivos():
    for i in range(5):
        with open(F'arquivo{i}.txt', 'w') as file:
            file.write('Criamos um novo arquivo')
            sleep(1)
            console.log(f'Processando!')
            
           with console.status('[green]Realizando o processo....[/]') as arquivo:
                criar_arquivos()

              
# Logo

print(rf"""{Fore.MAGENTA}

___  ___     _                 _ _ _   _                 
|  \/  |    | |               | (_) | (_)                
| .  . | ___| |_ ___  ___   __| |_| |_ _  ___  _ __  ___ 
| |\/| |/ _ \ __/ _ \/ _ \ / _` | | __| |/ _ \| '_ \/ __|
| |  | |  __/ ||  __/ (_) | (_| | | |_| | (_) | | | \__ \
\_|  |_/\___|\__\___|\___/ \__,_|_|\__|_|\___/|_| |_|___/
                                
                                  Created by Kevin Ivanov

 ------------ Using wttr.in a console-oriented weather forecast ------------

{Fore.RESET}""")


city = input("\nEnter the city name : ")
url = "https://wttr.in/{}".format(city)
try:
    res = requests.get(url)
    print(res.text)
except:
    print("Error occure Please try again later...")
