r1 = float(input('Digite o valor da reta 1: '))
r2 = float(input('Digite o valor da reta 2: '))
r3 = float(input('Dogite o valor da reta 3: '))
soma = r2 + r3
sub = abs(r2 - r3)
if r1 < soma and r1 > sub:
    print('Esses três comprimentos podem formar um TRIÂNGULO.')
else:
    print('Esses três comprimentos NÃO podem formar um TRIÂNGULO.')
