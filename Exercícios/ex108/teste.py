import moeda as md

p = float(input('Digite o preço: R$'))
print(f'A metade de {md.moeda(p)} é {md.moeda(md.metade(p))}\n'
      f'O dobro de {md.moeda(p)} é {md.moeda(md.dobro(p))}\n'
      f'Aumentando 10%, temos {md.moeda(md.aumentar(p, 10))}\n'
      f'Reduzindo 13%, temos {md.moeda(md.diminuir(p, 13))}')
