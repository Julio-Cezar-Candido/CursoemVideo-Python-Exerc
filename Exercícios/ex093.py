jogador = {'nome': str(input('Nome do jogador: ')).strip()}
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {p+1}? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print(f'{"-="*30}\n{jogador}\n{"-="*30}')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print(f'{"-="*30}\nO jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for k, v in enumerate(gols):
    print(f'    => Na partida {k+1}, fez {v} gol(s).')
print(f'Foi um total de {jogador["total"]} gol(s).')
