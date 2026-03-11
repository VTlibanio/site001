from rich import print
from rich.table import Table

tabela = Table(title="VT")
tabela.add_column('nome da empresa')
tabela.add_column('tabela de preço')

tabela.add_row('victor miguell', "59,000,000,000$")
tabela.add_row('sanidade mental', '[red]inestimável[/]')





print(tabela)
