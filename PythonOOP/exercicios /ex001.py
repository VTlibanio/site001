class Gafanhoto:
    def __init__(self):  # método construtor
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é aluno e tem {self.idade} de idade"

# Objetos e chamadas devem ficar FORA da classe
g1 = Gafanhoto()
g1.nome = ("maria")
g1.idade = 20
g1.aniversario()
print(g1.mensagem())
