from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
print(f'{"-="*15}\n{"JOGO DOS DADOS":^30}\n{"-="*15}')
for v in range(1, 5):
    jogadores[f'jogador {v}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado!')
    sleep(1)
print(f'{"-="*15}\n{"== RANKING DOS JOGADORES ==":^30}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}!')
    sleep(1)
print('-='*15)
