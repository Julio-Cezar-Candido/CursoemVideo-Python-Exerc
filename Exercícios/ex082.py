lista1 = [(int(input('Digite um valor: ')))]
lista2 = []
lista3 = []
while True:
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r == 'S':
        lista1.append(int(input('Digite um valor: ')))
    elif r == 'N':
        break
for c in lista1:
    if c % 2 == 0:
        lista2.append(c)
    else:
        lista3.append(c)
print(f'{"-="*30}\nA lista completa é {lista1}\n'
      f'A lista de pares é {lista2}\n'
      f'A lista de ímpares é {lista3}')
