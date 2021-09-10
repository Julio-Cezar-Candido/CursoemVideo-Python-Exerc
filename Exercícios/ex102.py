def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opicinal) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
    if not show:
        return f
    else:
        for c in range(n, 1, -1):
            print(f'{c} x ', end='')
        print(f'1 = {f} FIM!')


print("-" * 30)
print(fatorial(8, show=True))
#help(fatorial)
