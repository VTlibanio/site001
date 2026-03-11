from random import sample

j = int(input('Pra quantos jogos da Mega-Sena você deseja obter palpites? '))

jogos =[]#lista

for i in range(j):
    jogo = sorted(sample(range(0,61),6))#sorted sample simplismente faz sorteios com os numeros e range vai determinar quantas vezes isso acontece 
    jogos.append(jogo)#jogos recebe o valor de jogo 
    print(f'jogo{i+1} ; {jogo}')

print(f'\nBoa sorte nos {j} jogos.')