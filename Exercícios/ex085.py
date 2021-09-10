num = [[], []]
for n in range(1, 8):
    numero = int(input(f'Digite o {n}º valor: '))
    if numero % 2 == 0:
        num[0].append(numero)
    else:
        num[1].append(numero)
print(f'{"-="*30}\nOs valores pares digitados foram: {sorted(num[0])}\n'
      f'Os valores ímpares digitados foram: {sorted(num[1])}')
