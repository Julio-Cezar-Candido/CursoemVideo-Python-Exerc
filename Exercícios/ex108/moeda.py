def metade(p=0):
    valor = p / 2
    return valor


def dobro(p=0):
    valor = p * 2
    return valor


def aumentar(p=0, taxa=0):
    valor = p * (1 + (taxa / 100))
    return valor


def diminuir(p=0, taxa=0):
    valor = p * (1 - (taxa / 100))
    return valor


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')
