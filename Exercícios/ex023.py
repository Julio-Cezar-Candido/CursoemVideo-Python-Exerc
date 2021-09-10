valor = int(input('Digite um valor de 0 a 9999: '))
u = valor // 1 % 10
d = valor // 10 % 10
c = valor // 100 % 10
m = valor // 1000 % 10
print ('Analisando o número {}...\nA unidade é: {}\nA dezena é: {}'
       '\nA centena é: {}\nA milhar é: {}'.format(valor, u, d, c, m))
