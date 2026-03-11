dados = []  # Renomeei 'dict' para 'dados' pra evitar confusão com o tipo built-in do Python, mas a ideia é a mesma
nome = str(input('nome:'))
media = float(input('media:'))
if media < 7:
    situação = 'reprovado'
else:
    situação = 'aprovado'
dados.append(nome)  # Adiciona o nome à lista
dados.append(media)  # Adiciona a média à lista
dados.append(situação)  # Adiciona a situação à lista (essa é a parte nova que você pediu)
print('nome : ' + str(dados[0]))  # Exibe o nome
print('média : ' + str(dados[1]))  # Exibe a média
print('a situação é ' + dados[2])  # Exibe a situação