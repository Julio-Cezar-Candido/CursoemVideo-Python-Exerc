compras = ('Lápis', 0.5, 'Borracha', 0.75, 'Caderno', 27.99, 'Estojo', 25,
           'Compaso', 18.5, 'Mochila', 15, 'Caneta', 1.5, 'Agenda', 30,
           'Folhas A4', 22)
print(f'{"-"*40}\n{"LISTAGEM DE PREÇOS":^40}\n{"-"*40}')
for item in range(0, len(compras)):
    if item % 2 == 0:
        print(f'{compras[item]:.<30}', end='')
    else:
        print(f'R$ {compras[item]:>4.2f}')
print(f'{"-"*40}')
