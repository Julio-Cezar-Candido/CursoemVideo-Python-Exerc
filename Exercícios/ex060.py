n = int(input('Digite um número para calcular seu fatorial: '))
print(f'Calculando {n}! = ', end='')
cont = 1
while n != 0:
    print(f'{n}', end='')
    print(' x ' if n > 1 else ' = ', end='')
    cont *= n
    n = n - 1
print(f'{cont}')
