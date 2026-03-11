class Gafanhoto:
    def __init__(self, nome = "Vazio", idade = 0):  # método construtor
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self): # dunder methode
        return f"{self.nome} é aluno e tem {self.idade} de idade"

    def __getstate__(self):
        return f"nome é: {self.nome}, e a idade = {self.idade}"

# Objetos e chamadas devem ficar FORA da classe
g1 = Gafanhoto('Maria', 17)

print(g1.__getstate__())

g2 = Gafanhoto('Mauro', 78)
print(g2.__getstate__())