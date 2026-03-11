galera = list()# aque sào duas listas 
dados = list()
while True:
    dados.append(str(input('digite seu nome: ')))
    dados.append(float(input('seu peso em (kg): ')))
    escolha = input('deseja comtinuar ? [S/N]')
    galera.append(dados[:])# isso vai criar uma copia da lista de dados 
    dados.clear()
    if escolha in ('N','Não', 'n', 'não'):
        break
    if escolha not in ('sim','S','s','SIM','N','NAO','n','nao'):
        print('tente novamente...')
        escolha = input('deseja continuar ?')
        if escolha in ('N','Não','n','não'):
            break
        else:
            continue

pesos = [p[1] for p in galera]
media = sum(pesos) / len (pesos)


mais_pesados = [p for p in galera if p[1] > media]
mais_leves = [p for p in galera if p[1] < media]


for p in galera:
    print(f'o peso do {p[0]} é {p[1]} (Kg)')
print(f'total de {len(galera)} pessoas cadastradas.')

print(f'As pessoas mais leves são: {mais_leves}')
print(f'E as pessoas masi pesadas são: {mais_pesados}')