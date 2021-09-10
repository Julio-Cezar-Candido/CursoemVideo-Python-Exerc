from math import sin, cos, tan, radians
a = float(input('Digite o valor do ângulo: '))
r = radians(a)
print(f'O valor do seno, cosseno e tangente é igual respctivamente à:'
      f' {sin(r):.2f}, {cos(r):.2f} e {tan(r):.2f}')
