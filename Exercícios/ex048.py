s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('O somatório de todos os {} números ímpares múltiplos de três foi {}!'.format(cont, s))
