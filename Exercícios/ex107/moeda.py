def metade(p):
    valor = p / 2
    return f'{valor:.2f}'


def dobro(p):
    valor = p * 2
    return f'{valor:.2f}'


def aumentar(p, taxa):
    valor = p * (1 + (taxa/100))
    return f'{valor:.2f}'


def diminuir(p, taxa):
    valor = p * (1 - (taxa/100))
    return f'{valor:.2f}'
