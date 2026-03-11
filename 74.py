import random

sorteados = random.sample(range(1,10), 5) # é extamente a mesma coisa que random choice so que o sample é pra sortear mais de um 
print(sorteados)

menor = min(sorteados) #min e max serve literalmente pra achar o menor e o maior dentro de uma tupla ou lista.
maior = max(sorteados)

print(f'numeros sorteados são : {sorteados}')# melhor maneira de usar f string é assim
print(f'O maior número da lista é {maior}')
print(f'E o menor numero da lista é {menor}')
