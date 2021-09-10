valores = [(int(input('Digite um valor: ')))]
while True:
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r == 'S':
        valores.append(int(input('Digite um valor: ')))
    elif r == 'N':
        break
valores.sort(reverse=True)
print(f'{"-="*30}\nVocê digitou {len(valores)} elementos.\n'
      f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encotrado na lista!')
