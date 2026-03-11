from time import sleep

def maior (*num):
    cont = maior = 0
    print('analizando valores passados...')
    for valor in num:
        print(f'{valor}',end=' ')
        sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1    
    print(f'foram informados {cont} valores')
    print(f'o maior valor foi {maior}')

maior(2,4,5,6,2,9,)
maior(2,2,6,7,88,8,)
maior(3,4,2,8,9)