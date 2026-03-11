listapares = []
listaimpares = []# listas

matriz = [0] * 9
for i in range(9):
    linha = i // 3
    coluna = i % 3 
    matriz[i]= int(input('digite seu valor  ; '))
    if matriz[i] % 2 == 0:
        listapares.append(matriz[i])
    else:
        listaimpares.append(matriz[i])

somapares = sum(listapares)# faz a soma dos numeros de ambas as listas
somaimpares = sum(listaimpares)


print('='*60)
for i in range(0, 9, 3):
    print(f'[{matriz[i]:^5}][{matriz[i +1 ]:^5}][{matriz[i+2]:^5}]')

print(f' os numeros impares são: {listaimpares}')
print(f' os numeros pares são: {listapares}')  
print(f'a soma dos valores impares são: {somaimpares}')
print(f' a soma dos valores pares são: {somapares}')