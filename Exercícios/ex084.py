dados = []
pessoas = []
maior = menor = 0
contmaior = contmenor = 1
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        menor = maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
    while resp != 'S':
        resp = str(input('Opção ÍVALIDA! Quer continuar? [S/N]')).strip().upper()[0]
print(f'{"-="*30}\nAo todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for dado in pessoas:
    if dado[1] == maior:
        print(f'[{dado[0]}] ', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for dado in pessoas:
    if dado[1] == menor:
        print(f'[{dado[0]}] ', end='')
