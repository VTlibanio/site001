pesos = []  # Lista para guardar TODOS os pesos

for c in range(0, 4):
    peso = float(input('digite seu peso: '))  # Converte string → float
    pesos.append(peso)  # Adiciona na lista

media = sum(pesos) / len(pesos)  # Agora pesos é lista: [70.5, 65.0, ...]
print(f'Média: {media}')
