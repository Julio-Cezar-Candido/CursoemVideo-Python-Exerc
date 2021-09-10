perguta = 'S'
cont = maior = menor = soma = media = 0
while perguta in 'Ss':
    n = float(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    perguta = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
media = soma/cont
print('Você digitou {} números e a média entre eles foi {:.2f}\n'
      'O maior número digitado foi {} e o menor foi {}\n'.format(cont, media, maior, menor))
