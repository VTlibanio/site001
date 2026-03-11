from ex115.lib.interface import leiaInt
from lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    CriarArquivo(arq)



while True:
    opc = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if opc == 1:
        lerArquivo(arq)
        print('Opção 1 selecionada...')
    elif opc == 2:
        cabecalho('novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('idade: ')
        cadastrar(arq, nome, idade)
    elif opc == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(1)
