n1 = float(input('\033[34mDigite um valor: '))
n2 = float(input('Digite mais um valor: \033[m'))
print('\033[5;32mANALISANDO...\033[m')
if n1 > n2:
    print('\033[36mO valor {} é maior que o valor {}.'.format(n1, n2))
elif n2 > n1:
    print('\033[36mO valor {} é maior que o valor {}.'.format(n2, n1))
else:
    print('\033[36mNão existe valor maior, os dois valores {} e {} são iguais.'.format(n1, n2))
