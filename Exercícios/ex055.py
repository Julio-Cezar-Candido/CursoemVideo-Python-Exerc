maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}º pessoa: Kg '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg\n'
      'O menor peso foi de {}Kg'.format(maior, menor))
