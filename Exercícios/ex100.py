from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valore da lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 5))
        print(lista[c], end=' ')
        sleep(0.5)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}')


v = []
sorteia(v)
somaPar(v)
