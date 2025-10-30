from rich.console import Console
from rich.table import Table
from rich import print

print('ola [bold magenta]mundo[/bold magenta]')
print("isso e um [on_red]ERRO[/on_red]!")

console = Console()
tabela = Table(title='meu quiz')

tabela.add_column('pergunta', style='cyan')
tabela.add_column('resposta', style='green')

tabela.add_row('capital do japao?', 'toquio')
tabela.add_row('2 + 2', '4')

console.print(tabela)

