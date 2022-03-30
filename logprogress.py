from rich.console import Console
from time import sleep

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
