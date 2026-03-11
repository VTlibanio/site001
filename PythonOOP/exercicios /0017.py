from rich import print
from rich.panel import Panel


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return f"Produto: {self.nome} - Valor: R$ {self.valor:,.2f}"

    def etiqueta(self):
        # Linha 1: Nome centralizado
        linha1 = self.nome.center(30, ' ')

        # Linha 2: Separador
        linha2 = '-' * 30

        # Linha 3: Preço formatado e centralizado
        precof = f"R$ {self.valor:,.2f}".center(30, ' ')

        conteudo = f"{linha1}\n{linha2}\n{precof}"

        etiqueta = Panel(conteudo, title="[bold blue]PRODUTO[/bold blue]",
                         width=34, border_style="cyan")
        print(etiqueta)


p1 = Produto("iPhone 17 Pro Max 256GB", 18900.00)
p1.etiqueta()
