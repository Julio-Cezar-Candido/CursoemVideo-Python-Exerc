km = float(input('Qual é a distância da sua viagem? Km:'))
if km <= 200:
    print('O valor da sua passagem será R${:.2f}'.format(km * 0.5))
else:
    print('O valor da sua passagem será R${:.2F}'.format(km * 0.45))
