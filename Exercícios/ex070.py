print(f'{"-"*34}\n{"LOJA J.C.SILVA":^34}\n{"-"*34}')
menorprec = cont = nomebarato = cont1000 = soma = 0
while True:
    nome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    soma += preco
    cont += 1
    if preco > 1000:
        cont1000 += 1
    if cont == 1:
        nomebarato = nome
        menorprec = preco
    elif cont > 1:
        if menorprec > preco:
            menorprec = preco
            nomebarato = nome
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi R${soma:.2f}\n'
      f'Temos {cont1000} produto(s) custando mais de R$1000,00\n'
      f'O produto mais barato foi a "{nomebarato}", que custa R${menorprec:.2f}')
