galera = list()
pessoa = dict()
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO! Digite apenas F ou M.')

    pessoa['idade'] = int(input('Idade: '))

    galera.append(pessoa.copy())

    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if resp == 'N':
        break


media = sum(p['idade'] for p in galera) // len(galera)
print(f'\nA média de idade das pessoas cadastradas é {media}')
print(f'Ao todo são {len(galera)} pessoas cadastradas.')

print('\nAs mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print()

print('\nLista das pessoas com idade acima da média:')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():    
            print(f'  {k} = {v}')
        print()  # <-- Linha em branco entre pessoas

print('<<< Encerrado >>>')
