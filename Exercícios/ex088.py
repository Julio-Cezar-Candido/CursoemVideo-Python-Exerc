from time import sleep
from random import randint
palpites = []
palpite = []
print(f'{"-"*40}\n{"JOGA NA MEGA SENA":^40}\n{"-"*40}')
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
for p in range(0, quantidade):
    while True:
        seisnum = randint(1, 60)
        if seisnum not in palpite:
            palpite.append(seisnum)
        if len(palpite) == 6:
            break
    palpite.sort()
    palpites.append(palpite[:])
    palpite.clear()
print(f'{"-="*3}  SORTEANDO {quantidade} JOGOS   {"-="*3}')
for i, p in enumerate(palpites):
    print(f'Jogo {i+1}: {p}')
    sleep(1)
print(f'{"-="*4} < BOA SORTE! > {"-="*4}')
