numeros = []
for n in range(5):
    num = int(input('digite seu valor: '))
    numeros.append(num)
    numeros.sort()

print(f'os valores adicionados e em ordem correta: {numeros}')