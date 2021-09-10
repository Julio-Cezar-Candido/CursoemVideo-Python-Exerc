print('{}\n'
      ' 10 TERMOS DE UMA PA\n'
      '{}'.format('=='*12, '=='*12))
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 10
termo = primeiro
quantermo = 0
while cont != 0:
    print('{} > '.format(termo), end='')
    cont -= 1
    termo += razao
    quantermo += 1
    if cont == 0:
        print('Pausa')
        perguta = int(input('Você quer ver mais algum termo?\nSe sim quantas? Se não Digite 0: '))
        cont = perguta
print('Prgressão finalizada com {} termos'.format(quantermo))
