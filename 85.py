def new_func():
    listapar = []
    listaimpar = []

    for c in range(7):
        valor = int(input('digite seu valor: '))

        if valor % 2 == 0:
            listapar.append(valor)
        else:
            listaimpar.append(valor)

    lista = listaimpar + listapar 
    lista.sort()
    listapar.sort()
    listaimpar.sort()

    print(f'lista final: {lista}')
    print(f'lista de números impares:{listaimpar}')
    print(f'lista de números pares: {listapar}')

new_func()
