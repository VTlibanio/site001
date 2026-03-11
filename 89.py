listageral = []
while True:
    nomealuno = input('digite seu nome:')
    nota1 = float(input('digite sua nota: '))
    nota2 = float(input('digite sua nota: '))
    media = nota1+nota2 / 2
    listageral.append([nomealuno,nota1,nota2,media])# lista vai receber nome, nota 1 e nota 2 e a media de cada aluno.


    escolha = input('deseja continuar ? :[S/N]').upper()
    if escolha in ['N', 'NAO', 'NÃO']:
        break
    if escolha not in ['S', 'SIM']:
        print('Tente novamente...')

print('\n' + '='*60)
print(f"{'Nº':>3} {'NOME':^20} {'NOTA 1':^8} {'NOTA 2':^8} {'MÉDIA':^8}")
print('='*60)
for i, aluno in enumerate(listageral, 1):
    print(f'{i:>3} {aluno[0]:^20} {aluno[1]:>7.1f} {aluno[2]:>7.1f} {aluno[3]:>7.1f}')
print('='*60)