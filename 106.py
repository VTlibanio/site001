from time import sleep

def ajuda(comando):
    print('\033[34m')  # Azul
    print('=' * 42)
    print(f'  Acessando o manual do comando "{comando}"')
    print('=' * 42)
    print('\033[33m')  # Amarelo
    help(comando)
    print('\033[m', end='')  # Reset
    sleep(2)

def leiaInt(msg):
    while True:
        try:
            n = input(msg)
            if n.isnumeric():
                return int(n)
            else:
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')

# Programa principal
while True:
    print('\033[32m')  # Verde
    print('~' * 42)
    print('         SISTEMA DE AJUDA')
    print('~' * 42)
    print('\033[33m')
    funcao = str(input('Função ou "FIM" para sair: ')).strip().lower()
    print('\033[m', end='')
    
    if funcao == 'fim':
        print('\033[31mAté logo!\033[m')
        break
    else:
        ajuda(funcao)

