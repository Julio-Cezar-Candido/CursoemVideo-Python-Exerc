contmul = conthom = cont = 0
while True:
    print(f'{"-"*34}\n{"CADASTRE UMA PESSOA":^34}\n{"-"*34}')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]'))
    if idade > 18:
        cont += 1
    if sexo == 'M':
        conthom += 1
    if sexo == 'F' and idade < 20:
        contmul += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{"-"*34}\nTotal de pessoas com mais de 18 anos: {cont}\n'
      f'Ao todo temos {conthom} homem(ns) cadastrado(s).\n'
      f'E temos {contmul} mulherer(es) com menos de 20 anos.')
