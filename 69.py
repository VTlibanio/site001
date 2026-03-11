tot18 = homem = mulheresmenos20 = 0

while True:
    idade = int(input('Digite a sua idade: '))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Digite seu gênero [M/F]: ').strip().upper()[0]
    
    # maiores de 18
    if idade >= 18:
        tot18 += 1
    
    # homens
    if sexo == 'M':
        homem += 1
    
    # mulheres com menos de 20
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1

    # continuar?
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    
    if resp == 'N':
        break

print('Acabou!')
print(f'Total de pessoas com 18 anos ou mais: {tot18}')
print(f'Total de homens cadastrados: {homem}')
print(f'Total de mulheres com menos de 20 anos: {mulheresmenos20}')
