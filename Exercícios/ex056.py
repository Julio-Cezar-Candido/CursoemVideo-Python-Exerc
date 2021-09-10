media = 0
nomeMaisVelho = 0
mulherMenos20 = 0
idadeMaisVelho = 0
for p in range(1, 5):
    print('---- {}º PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    if sexo == 'M':
        if p == 1:
            idadeMaisVelho = idade
            nomeMaisVelho = nome
        elif idadeMaisVelho < idade:
            nomeMaisVelho = nome
            idadeMaisVelho = idade
    if sexo == 'F':
        if idade < 20:
            mulherMenos20 += 1
print('\nA média de idade das pessoas foi de {:.2f}\n'
      'O homem mais velho tem {} e se chama "{}"\n'
      'Dentre essas pessoas existe {} mulher(es) menores de 20 anos'
      .format(media/p,idadeMaisVelho, nomeMaisVelho, mulherMenos20))
