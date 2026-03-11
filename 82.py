numeros = []
pares = [] # aqui eu criei 3 listas 
impares = []
while True: # enqutanto for verdadeiro, continue...
    num = int(input('valor: :'))
    numeros.append(num)# com esse append, automaticamente o valor de num vai pra numeros, a listinha que eu criei

    escolha =  input('deseja continuar ? [N/S] :')
    if escolha in ['N', 'n' , 'não']:  # Sai só com N
        break

numeros.sort()# isso vai organizar os numeros do menor para o maiorm

for n in numeros: # para cada numero dentro de numeros ele vai verificar se é par ou impar 
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()#...............apenas organização
numeros.sort()
impares.sort()


print(f'os seus valores impares são: {impares}')
print(f'seus valores pares são : {pares}')