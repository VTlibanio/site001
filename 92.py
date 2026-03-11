# Importa a classe datetime para pegar o ano atual automaticamente.
# Isso permite calcular a idade e o tempo para aposentadoria.
from datetime import datetime

# Cria um dicionário chamado 'dados'.
# O exercício pede para armazenar tudo dentro de um dicionário.
dados = {}

# Lê o nome e armazena na chave 'nome' do dicionário.
dados['nome'] = str(input('Nome: '))

# Lê o ano de nascimento.
# Vamos usar esse valor para calcular a idade atual.
nasc = int(input('Ano de nascimento: '))

# Calcula a idade atual usando o ano atual do sistema.
# datetime.now().year retorna o ano atual (ex.: 2025).
dados['idade'] = datetime.now().year - nasc

# Lê o número da Carteira de Trabalho (CTPS).
# Se for 0, significa que a pessoa não tem carteira.
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

# Verifica se a pessoa possui carteira de trabalho.
# Se NÃO tiver (ctps == 0), o programa não pedirá mais dados.
if dados['ctps'] != 0:
    # Lê o ano da contratação.
    # Esse dado é necessário para calcular a aposentadoria.
    dados['contratacao'] = int(input('Ano da contratação: '))

    # Lê o salário em reais, como número decimal.
    dados['salario'] = float(input('Salário: R$ '))

    # Calcula em que idade a pessoa vai se aposentar.
    #
    # Fórmula:
    # idade atual + (ano da contratação + 35 anos de contribuição - ano atual)
    #
    # Exemplo:
    # 17 + (2023 + 35 - 2025) = 17 + 33 = 50 anos
    #
    # Isso significa que com 50 anos a pessoa cumpre 35 anos de contribuição.
    dados['aposentadoria'] = dados['idade'] + (dados['contratacao'] + 35 - datetime.now().year)

# Linha decorativa só para separar visualmente o resultado.
print('-' * 60)

# Exibe todos os dados armazenados no dicionário.
# O loop percorre a chave (k) e o valor (v) de cada item.
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
