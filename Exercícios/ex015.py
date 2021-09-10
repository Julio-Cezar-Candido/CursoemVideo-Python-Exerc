d = int(input('Informe a quantidade de dias usando o carro: '))
k = float(input('Informe a quantidade de kilometros percorridos: '))
v = (d*60) + (k*0.15)
print (f'O total a pagar pelo aluguel do carro, que foi usado por {d} dias e que rodou {k}km, é de {v:.2f} reais.')
