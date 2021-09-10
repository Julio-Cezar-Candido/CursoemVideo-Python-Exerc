pessoas = list()
soma = 0
while True:
    pessoa = {'Nome': str(input('Nome: ')).strip()}
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if r == 'N':
        break
print(f'{"-="*30}\nA) O grupo tem {len(pessoas)} pessoas.\n'
      f'B) A média de idade é de {soma/len(pessoas):.2f} anos.\n'
      f'C) As mulheres cadastradas foi(ram): ', end='')
for i in pessoas:
    if i['Sexo'] == 'F':
        print(f'{i["Nome"]};', end=' ')
print(f'\nD) Lista das pessoas que estão acima da média:')
for i in pessoas:
    if i['Idade'] > soma/len(pessoas):
        print('    ', end='')
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRANDO >>')
