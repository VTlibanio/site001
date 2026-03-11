numeros = []
while True:
    num =  int(input('digite seu valor :'))
    if num in numeros:
        print(f'{num} já existem na lista...')
        break

    numeros.append(num)
    numeros.sort()
    print(f'Lista atual: {numeros}')