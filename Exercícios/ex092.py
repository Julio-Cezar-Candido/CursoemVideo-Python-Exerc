from datetime import date
pessoa = {'Nome': str(input('Nome: ')).strip()}
nasc = int(input('Ano de nascimento: '))
pessoa['Idade'] = date.today().year - nasc
pessoa['CTPS'] = int(input('Carteira de Trabalho: (0 não tem) '))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Sálario'] = float(input('Sálario: R$'))
    pessoa['Aposentadoria'] = (35 + pessoa['Contratação']) - nasc
print("-=" * 30)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
