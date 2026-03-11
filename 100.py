from random import randint
from time import sleep

def sorteia (lista):
    print('sorteando valores da lista', end=' ')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        sleep(0.2)
    print('pronto.')


def somapar(lista):
    soma = 0 
    for valor in lista:
        if valor % 2 == 0:
            soma +=valor
    print(f'somando os valores pares {lista} temos {soma} em soma total dos pares...')        

numeros = list()
sorteia(numeros)
somapar(numeros)