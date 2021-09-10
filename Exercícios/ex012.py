v = float(input('Qual é o valor do produto que deseja comprar? R$'))
nv = v*0.95
d = v*0.05
print(f'Com um desconto de 5%, a vista, você irá pagar apenas R${nv:.2f} neste produto.'
      f'\nRecebendo um desconto de R${d:.2f}.')