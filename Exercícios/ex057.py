sexo = str(input('Digite um sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Sexo invalido! Por favor tente novamente: [M/F]: ')).strip().upper()
if sexo == 'M':
    print('Sexo MASCULINO regitrado com sucesso!')
else:
    print('Sexo registrado FEMININO com sucesso!')
