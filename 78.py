valores = []

for v in range (0, 5):
    valor = int(input('digite seus valores :'))
    valores.append(valor)

menor = min(valores)
maior = max(valores)

pos_menor = valores.index(menor)
pos_maior = valores.index(maior)

print(f'meu maior valor é {maior} nas posições {pos_maior}')
print(f'meu menor valor é {menor} nas posições {pos_menor}')
print(f'essa lista tem {len(valores)} elementos.')
