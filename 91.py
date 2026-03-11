# Importa o módulo 'random' da biblioteca padrão do Python.
# Este módulo fornece funções para gerar números aleatórios, essenciais para simular lançamentos de dados.
import random

# Inicializa um dicionário vazio chamado 'jogadores'.
# Dicionários em Python são estruturas que armazenam pares chave-valor.
# Usaremos o nome do jogador como chave e sua pontuação (valor do dado) como valor.
# Exemplo: {'João': 4, 'Maria': 6}.
jogadores = {}

# Inicia um loop 'for' que itera sobre um range de 1 a 4 (inclusive).
# 'range(1, 5)' gera os números 1, 2, 3 e 4, representando os quatro jogadores.
# Cada iteração pedirá o nome e sorteará o valor do dado para um jogador.
for i in range(1, 5):
    # Solicita ao usuário o nome do jogador atual.
    # O f-string insere o número do jogador dinamicamente na mensagem.
    # '.strip()' remove espaços extras no início ou fim da digitação.
    nome = input(f'Nome do {i}º jogador: ').strip()
    
    # Verifica se o nome inserido está vazio.
    # Caso esteja, atribui um nome padrão como "Jogador 1".
    if not nome:
        nome = f'Jogador {i}'
    
    # Gera um número aleatório entre 1 e 6 usando 'random.randint()'.
    # Isso simula um lançamento de dado comum.
    valordado = random.randint(1, 6)

    # Adiciona o par nome → valor do dado ao dicionário.
    jogadores[nome] = valordado

    # Exibe o resultado do lançamento do dado para cada jogador.
    print(f'{nome} tirou {valordado} no dado.')

# Ordena os itens do dicionário 'jogadores' pelo valor do dado.
# 'jogadores.items()' retorna tuplas do tipo (nome, valor).
# 'key=lambda x: x[1]' diz ao 'sorted' para ordenar pelo valor da tupla (o valor do dado).
# 'reverse=True' garante que fique do maior para o menor.
jogadores_ordenados = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

# Exibe um ranking final com base nos valores ordenados.
print("\nRanking final:")
# 'enumerate' adiciona números (posição no ranking), começando em 1.
for posicao, (nome, valor) in enumerate(jogadores_ordenados, start=1):
    # Exibe o nome do jogador e sua pontuação na posição correspondente do ranking.
    print(f"{posicao}º lugar: {nome} com {valor}")
