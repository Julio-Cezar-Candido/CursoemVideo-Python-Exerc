valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'{"=-" * 24}\nVocê digitou os valores {valores}\n'
      f'O maior valor digitado foi {max(valores)} ', end='')
if valores.count(max(valores)) > 1:
    print('nas possições ', end='')
    for pos, c in enumerate(valores):
        if c == max(valores):
            print(f'{pos}...', end=' ')
else:
    print(f'na posição {valores.index(max(valores))}.\n')
print()
print(f'O menor valor digitado foi {min(valores)} ', end='')
if valores.count(min(valores)) > 1:
    print('nas possições ', end='')
    for pos, c in enumerate(valores):
        if c == min(valores):
            print(f'{pos}...', end=' ')
else:
    print(f'na posição {valores.index(min(valores))}.')
