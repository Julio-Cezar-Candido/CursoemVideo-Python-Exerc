import moeda as md

p = float(input('Digite o preço: R$'))
print(f'A metade de {md.moeda(p)} é {md.metade(p, True)}\n'
      f'O dobro de {md.moeda(p)} é {md.dobro(p, True)}\n'
      f'Aumentando 10%, temos {md.aumentar(p, 10, True)}\n'
      f'Reduzindo 13%, temos {md.diminuir(p, 13, True)}')
