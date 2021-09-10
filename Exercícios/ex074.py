from random import randint
sorteio = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'Os valores sorteados foram: ', end='')
valor = maior = menor = cont = 0
for núm in sorteio:
    print(f'{núm} ', end='')
    '''valor = núm
    cont += 1
    if cont == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
print(f'O maior valor sorteado foi: {maior}\n'
      f'O menor valor sorteado foi: {menor}')'''
print(f'\nO maoior valor sorteado foi: {max(sorteio)}\n'
      f'O menor valor sorteado foi: {min(sorteio)}')
