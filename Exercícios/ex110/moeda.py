def metade(p=0, form=False):
    valor = p / 2
    return valor if form is False else moeda(valor)


def dobro(p=0, form=False):
    valor = p * 2
    return valor if form is False else moeda(valor)


def aumentar(p=0, taxa=0, form=False):
    valor = p * (1 + (taxa / 100))
    return valor if form is False else moeda(valor)


def diminuir(p=0, taxa=0, form=False):
    valor = p * (1 - (taxa / 100))
    return valor if form is False else moeda(valor)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')


def resumo(p=0, aum=0, red=0):
    print(f'{"-"*34}\n'
          f'{"RESUMO DO VALOR".center(34)}\n'
          f'{"-"*34}\n'
          f'Preço analisado: \t{moeda(p)}\n'
          f'Dobro do preço: \t{dobro(p, True)}\n'
          f'Metade do preço: \t{metade(p, True)}\n'
          f'{aum}% de aumento: \t{aumentar(p, aum, True)}\n'
          f'{red}% de redução: \t{diminuir(p, red, True)}\n'
          f'{"-"*34}')
