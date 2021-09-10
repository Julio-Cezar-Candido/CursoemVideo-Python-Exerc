from datetime import date
atual = date.today().year
ano = int(input('Qual ano você nasceu? '))
idade = atual - ano
if idade <= 9:
    print('Você tem {} anos. Sua categoria é de nadador MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos. Sua categoria é de nadador INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos. Sua categoria é de nadador JUNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos. Sua categoria é de nadador SÊNIOR'.format(idade))
else:
    print('Você tem {} anos. Sua categoria é de nadador MASTER'.format(idade))
