import moeda as md

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {md.metade(p)}\n'
      f'O dobro de {p} é {md.dobro(p)}\n'
      f'Aumentando 10%, temos {md.aumentar(p, 10)}\n'
      f'Reduzindo 13%, temos {md.diminuir(p, 13)}')
