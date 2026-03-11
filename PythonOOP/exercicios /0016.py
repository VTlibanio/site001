from rich import print

class Rh:


    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return f" olá, sou {self.nome.capitalize()} e sou do setor de {self.setor} meu cargo é {self.cargo}👩🏼‍💻"


c1 = Rh("maria", "arquitetura", "administrativo")
print(c1)

