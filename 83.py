def validar_expressao(expressao):
    pilha = [] # apenas uma lista com o nome de pilha, mas poderia ser qualquer outro nome do planeta terra 

    for caractere in expressao: # para cada caractere na expressão ele vai fazer a vrificação 
        if caractere == '(': #vai verificar se existe ( na expressão
            pilha.append(caractere) #vai adicionar caractere em pilha
        elif caractere == ')': # vai verificar se ) já está em pilha
            if not pilha: # se não estiver la automaticamente não é valida
                return False #Essa linha retorna  False  imediatamente quando encontra um  )  sem um  (  correspondente na pilha. Isso detecta casos inválidos como  ")"  ou  "())" , onde há fechamento prematuro sem abertura prévia.
            pilha.pop() # vai arrancar o primeiro item da lista, então vai arrancar o (

    return len(pilha) == 0  # ESTA LINHA TEM QUE FICAR FORA DO FOR


print('===VALIDADOR DE EXPRESSÃO===\n')
expressao = input('digite sua expressão : ') # aqui a pessoa vai adicionar a expressão que ela deseja saber se é valida ou não 

if validar_expressao(expressao): # aqui ele vai verificar e verificar a expressão é valida baseada na extrutura que criamos acima 
    print('EXPRESSÃO VALIDA')
else:
    print('EXPRESSÃO INVALIDA, TENTE NOVAMENTE AO INICIAR PROGRAMA...')


    # basicamente esse mini programa serve pra verificar se todo parentese que abriu também fechou, se fechou é valido, se não é invalido...