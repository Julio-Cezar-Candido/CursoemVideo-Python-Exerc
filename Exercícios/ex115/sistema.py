from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArquivo(arq)


while True:
    perguta = menu(['Ver pessoas cadatradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if perguta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif perguta == 2:
        # Opção de cadastrar nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = cadastrarNome()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif perguta == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        cor('ERRO: Digite uma opção válida!', 1, False)
    sleep(2)
