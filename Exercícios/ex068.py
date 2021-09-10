from random import randint
cont = 0
print(f'{"=-"*14}\nVAMOS JOGAR PAR OU ÍMPAR\n{"=-"*14}')
while True:
    computador = randint(1, 10)
    valor = int(input('Diga um valor: '))
    jogador = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    while jogador not in 'PI':
        jogador = str(input('Par o Ímpar? [P/I] ')).strip().upper()[0]
    total = computador + valor
    if total % 2 == 0:
        print(f'{"-"*53}\nVocê jogou {valor} e o computador {computador}. Total de {total} DEU PAR\n{"-"*53}')
    elif total %2 != 0:
        print(f'{"-"*53}\nVocê jogou {valor} e o computador {computador}. Total de {total} DEU ÍMPAR\n{"-"*53}')
    if (jogador == 'P' and total %2 == 0) or (jogador == 'I' and total %2 != 0):
        cont += 1
        print(f'{"=-"*13}\nVocê VENCEU!\nVamos jogar novamente...\n{"=-"*13}')
    elif (jogador == 'P' and total %2 != 0) or (jogador == 'I' and total %2 == 0):
        print(f'{"=-" * 7}\nVocê PERDEU!\n{"=-" * 7}')
        break
print(f'GAMER OVER! Você venceu {cont} vezes.')
