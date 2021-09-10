def área(c, l):
    a = c * l
    print(f'A área de um terreno com dimenssões {c:.2f}m por {l:.2f}m é igual a {a:.2f}m²')


def lin():
    print("-=" * 15)


lin()
print('CALCULO DE ÁREA DE UM TERRENO')
lin()
c = float(input('Comprimento (m): '))
l = float(input('Largura (m): '))
lin()
área(c, l)
