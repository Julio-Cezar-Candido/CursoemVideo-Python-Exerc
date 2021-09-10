n = int(input('Digite um número para calcular seu fatorial: '))
print('Calculando {}! = '.format(n), end='')
cont = 1
while n != 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    cont *= n
    n = n - 1
print('{}'.format(cont))
