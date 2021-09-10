def metade(p=0, form=False):
    valor = p / 2
    '''if form:
        return f'R${valor:.2f}'.replace('.', ',')
    else:
        return valor'''
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
    return f'{moeda}{p:.2f}'.replace('.', ',')
