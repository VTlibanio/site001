print('='*70)
print('MERCADO DO VT'.center(65))
print('='*70)

produtos = [
    ("pão", 7.5),
    ("margarina", 10.00),
    ("batata", 18.50),
    ("esterminador de baratas", 36.89)
]

for nome, preco in produtos:# o que vai acontecer é f é ora formatar, . 60* vai adicionar 60 caracteres na frente do nome que o len vai ler, e pos isso o len preco entra na jogada, ficando na frente dos 60 caracteres. o primeiro len serve pra fazer a contagem dos caracteres que ha em numero e o ultimo server pra exibir no terminal  
    print(f"{nome}{'.'*(60 - len(nome) - len(f'{preco:.2f}'))}{preco:.2f}")
print('='*60)