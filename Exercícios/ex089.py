boletim = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], média])
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Resposta ÍNVALIDA! Por favor, tente novamente:\n'
                      'Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print(f'{"-=" * 30}\n{"No.":^4}{"NOME":<12}{"MÉDIA":>5}\n{"-" * 30}')
for pos, aluno in enumerate(boletim):
    print(f'{pos:<4}{aluno[0]:<12}{aluno[-1]:>5}')
while True:
    print('-' * 30)
    r = int(input('Mostrar notas de qual aluno (No.)? (999 interrompe): '))
    if r == 999:
        break
    if r >= len(boletim):
        print(f'{"-" * 30}\nOpção ÍVALIDA! Por favor, tente novamente.')
    elif r < 0:
        print(f'{"-" * 30}\nOpção ÍVALIDA! Por favor, tente novamente.')
    else:
        print(f'{"-"*30}\n'
              f'Notas de {boletim[r][0]} são: {boletim[r][1]}\n'
              f'{"-"*30}')
print('FINALIANDO...\nVolte Sempre!')
