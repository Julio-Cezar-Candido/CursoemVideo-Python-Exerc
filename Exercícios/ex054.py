from datetime import date
atual = date.today().year
passou = 0
naoPassou = 0
for idade in range(1, 8):
    nasc = int(input('Ano de nascimento da {}º pessoa?'.format(idade)))
    if 21 < atual - nasc:
        passou += 1
    else:
        naoPassou += 1
print('Ao todo tivemos {} pessoas maiores de idade\n'
      'E também tivemos {} pessoas menores de idade'.format(passou, naoPassou))
