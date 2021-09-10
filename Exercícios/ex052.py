numero = int(input('\033[35mDigite um número inteiro: '))
tot = 0
for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[34m', end='')
    print('{} '.format(c), end='')
if tot == 2:
    print('\n\033[35mO número digitado foi dividido \033[34m{}\033[35m, portanto o número \033[34m{} '
          '\033[31mé PRIMO'.format(tot, numero))
else:
    print('\n\033[35mO número digitado foi dividido \033[34m{}\033[35m, portanto o número \033[34m{} '
          '\033[31mNÃO é PRIMO'.format(tot, numero))
