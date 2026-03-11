numeros = [
    int(input('Digite um valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite outro valor: '))
]

print(f'Você digitou os valores: {numeros}')

# Contar quantas vezes o número 9 apareceu
cont9 = numeros.count(9)# numeros.count(9) vai buscar e contar pra ver qunatas vezes foi digitado o valor entre parenteses
print(f'O valor 9 aparece {cont9} vez(es)')

# Verificar se o número 3 foi digitado e em quais posições
if 3 in numeros:
    posicoes = [i + 1 for i, v in enumerate(numeros) if v == 3]  # i+1 para posição começar em 1 ( ele pega o valor e da a posição pra ele a aprtir de 1, entao tipo, valor 4 posicão 2) v in enumerate vai colocar as posiçoes nos numero e v == 3 vai achar em qual posição o 3 está
    print(f"O número 3 apareceu na(s) posição(ões): {', '.join(map(str, posicoes))}")

# Pegar números pares
pares = [v for v in numeros if v % 2 == 0] # ess V é apenas uma variavel t, então traduzindo, for é iteração, entao para cada elemento v in número, verificar se o resto da divisão por dois for 0 automaticamente esse mesmo numero é par. e ele vai fazer isso com todos os valores 

if pares:
    print(f"Números pares digitados: {', '.join(map(str, pares))}")
else:
    print("Nenhum valor par foi digitado...")
