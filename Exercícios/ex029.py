velocidade = int(input('Você passou a quantos Km/h na rodovia? km/h:'))
if velocidade > 80:
    print('Você passou da velocidade limite, levará uma multa de {} reais.'.format((velocidade - 80) * 7))
else:
    print('Você está dentro da velocidade permitida.\n !Parabéns! Você está dentro da LEI')
