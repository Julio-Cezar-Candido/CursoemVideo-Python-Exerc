h = float(input('Qual é a altura de sua parede em mestros? '))
l = float(input('Qual é a largura de sua parede em metros? '))
a = h*l
li = a/2
print(f'Será necessário {li:.3f} litros de tinta para que se possa pintar sua parede, o qual tem {a:.2f}m²')