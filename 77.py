palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for v in palavras:
    # aqui ele vai oegar cada palavra da lista e jogar pro maiusculo e o end vai ser prrenchido com o que vem abaixo
    print(f'\n Na palava {v.upper()} temos', end=' - ') # basicamente vai imprimir todas as palavras e jogalas pra maiusculo
    for letra in v: 
        if letra in 'aeiou': # para cada letra nas tuplas ele vai conferir se ela não é um aeiou
            print(letra, end='') # esse print o pc vai pegar so as vogais e jogar nesse espaço vazio do end. no primeiro print o pc já imprimiu todas as coisas, e nesse ultimo ele vai imprimir somente as vogais...
