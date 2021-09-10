from math import hypot
co = float(input('Digite o valor do cateto oposto do triagulo reto: '))
ca = float(input('Digite o valor do cateto adjacente do triagulo reto: '))
print(f'A valor da hipotenusa desse triagulo reto, cuja o cateto oposto tem '
      f'{co} e o adjacente tem {ca}, é igual a {hypot(co, ca):.2f}')
