totais = 0
numeros = []
while True:
    num = int(input('Digite seu valor (999 para parar): '))
    if num == 999:  # ← PARADA
        break
    
    totais += 1 
    numeros.append(num)
    numeros.sort(reverse=True)
    
    if 5 in numeros:
        print('o valor 5 foi digitado e está na lista')
    print(f'Lista atual: {numeros}')

print(f'Total de números: {totais}')
