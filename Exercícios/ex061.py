print('{}\n'
      ' 10 TERMOS DE UMA PA\n'
      '{}\n'.format('=='*12, '=='*12))
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
termo = primeiro
while cont <= 10:
    print('{} > '.format(termo), end='')
    cont += 1
    termo += razao
print('FIM!')
