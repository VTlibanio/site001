def leiaInt(msg=''):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não digitar esse número\033[m')
            n = 0
            break
        except:
            print('\033[1;31mERRO: por favor digite um número inteiro válido\033[m')
            continue
        else:
            return n

def leiaFloat(msg=''):
    while True:
        try:
            n = float(input(msg))
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não digitar esse número\033[m')
            n = 0.0
            break
        except:
            print('\033[1;31mERRO: por favor digite um número real válido\033[m')
            continue
        else:
            return n

# Programa principal
n1 = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
