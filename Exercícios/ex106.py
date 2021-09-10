from time import sleep

c = ('\033[m',  # 0 sem cores
     '\033[97;44m',  # 1 fundo azul
     '\033[97;42m',  # 2 fundo verde
     '\033[30;107m',  # 3 fundo branco
     '\033[30;41m',  # 4 fundo vermelho
     )


def escreva(texto, cor=0):
    print(c[cor], end='')
    print('~' * (len(texto) + 4))
    print(f'  {texto}')
    print('~' * (len(texto) + 4))
    print(c[0], end='')


def pyhelp(com):
    escreva(f'Acessando o manual do comando {com}', 1)
    sleep(1)
    print(c[3], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


# Programa principal
while True:
    escreva('SISTEMA DE AJUDA PyHELP', 2)
    ajuda = str(input('Função ou Biblioteca > ')).strip()
    if ajuda.upper() == 'FIM':
        sleep(1)
        break
    else:
        pyhelp(ajuda)
escreva('ATÉ LOGO!', 4)
