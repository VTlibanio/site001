from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    
    # Arruma o pulo pra ficar sempre positivo e bom!
    if p < 0:
        p = abs(p)  # Transforma negativo em positivo (melhor que p *= -1)
    if p == 0:
        p = 1       # Se zero, pula de 1 em 1

    if i > f:  # Conta PRA TRÁS (decrescente)
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
    else:  # Conta PRA FRENTE (crescente)
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')

# Testes do robô
contador(1, 10, 1)    # 1 2 3...10 FIM!
contador(10, 0, 2)    # 10 8 6...0 FIM!

print('Agora é sua vez:')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
