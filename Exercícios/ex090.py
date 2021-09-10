aluno = {'Nome': str(input('Nome: ')).strip()}
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'aprovado(a)'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'recuperação'
else:
    aluno['Situação'] = 'reprovado(a)'
print("-"*20)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
