print('{}\n'
      ' 10 TERMOS DE UMA PA\n'
      '{}\n'.format('=='*12, '=='*12))
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for c in range(primeiro, primeiro + (razao * 10), razao):
    print('{} > '.format(c), end='')
print('FIM')
