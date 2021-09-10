def player_status(nome = "<desconhecido>", gols = 0):
    '''if nome == '' and gols == '':
        print(f'O jogador <desconhecido> fez 0 gol(s) no campeonato.')
    elif nome == '':
        print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.')
    elif gols == '':
        print(f'O jogador {nome} fez 0 gol(s) no campeonato.')
    else:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')'''
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print(f'{"-"*20}')
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    player_status(gols=g)
else:
    player_status(n.strip(), g)
