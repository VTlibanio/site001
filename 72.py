num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
               'seis', 'sete', 'oito', 'nove', 'dez', 
               'onze', 'doze', 'treze', 'quatorze', 'quinze', 
               'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
        n = int(input('digite um numero de 0 á 20: '))
        if 0 <= n <=20:
            print(f'você digitpu o número {num_extenso[n]}')
            break
        else: 
            print('tente novamente!')