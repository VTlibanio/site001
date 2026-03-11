import random  # Importa a biblioteca para gerar números aleatórios
jogadores = {}  # Cria um dicionário vazio para armazenar os jogadores e seus valores de dados
# Loop para gerar valores para 4 jogadores
for jogador in range(1, 5):  # Roda 4 vezes, um para cada jogador (de 1 a 4)
    valordado = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6 (como um dado)
    jogadores[f'jogador {jogador}'] = valordado  # Adiciona ao dicionário: chave 'jogador X' com valor do dado
# Ordena os itens do dicionário pelos valores (do maior para o menor)
jogadores_ordenados = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
# sorted() cria uma lista de tuplas ordenadas; key=lambda x: x[1] ordena pela segunda parte (valor); reverse=True faz decrescente
# Encontra o vencedor (maior valor)
vencedor_chave = max(jogadores, key=jogadores.get)  # max() encontra a chave com o maior valor
vencedor_valor = jogadores[vencedor_chave]  # Pega o valor do vencedor usando a chave
# Exibe os resultados
print("Valores dos dados (ordenados do maior para o menor):")
for chave, valor in jogadores_ordenados:  # Loop pela lista ordenada
    print(f"{chave}: {valor}")  # Imprime cada jogador e seu valor
print(f"\nO vencedor é {vencedor_chave} com {vencedor_valor} pontos!")  # Imprime o vencedor
