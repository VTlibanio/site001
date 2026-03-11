from rich import print
from rich.panel import Panel

class Churrasco:
    consumomedio = 0.400
    precokg = 82.99

    def __init__(self, titulo, qtd):
        self.titulo = titulo
        self.participantes = qtd

    def __str__(self):
        return f'Esse é o {self.titulo} com {self.participantes} participantes!!!'

    def calcular_qtd_carne(self):  # ← Corrigido nome e return
        return self.participantes * Churrasco.consumomedio  # ← Nome correto

    def calcular_total(self):
        # Aqui você calcula total de carne
        return self.calcular_qtd_carne() * self.__class__.precokg

    def custoindividual(self):
        # Aqui você calcula custo por pessoa
        return self.calcular_total() / self.participantes


    def analisar(self):
        conteudo = f"[bold]Análise:[/]"
        conteudo += f"\nParticipantes: [blue]{self.participantes}[/]"
        conteudo += f"\nCarne total: [green]{self.calcular_qtd_carne():.1f}kg[/]"
        conteudo += f"\nCusto total: [red]R${self.calcular_total():,.2f}[/]"
        conteudo += f"\nCusto/pessoa: [yellow]R${self.custoindividual():,.2f}[/]"


        painel = Panel(conteudo, title=f"[bold cyan]{self.titulo}[/bold cyan]")
        print(painel)

c1 = Churrasco("Churras dos amigos", 22)
c1.analisar()

c2 = Churrasco("Festa do fim de ano", 90)
c2.analisar()

