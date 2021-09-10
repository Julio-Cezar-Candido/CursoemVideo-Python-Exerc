salario = float(input('Qual é o seu atual sálario? R$'))
if salario <= 1250.00:
    aumento = salario * 0.15
    atualsalario = salario + aumento
    print('O seu aumento será de R${:.2f}. Passando a ser R${:.2f}.'.format(aumento, atualsalario))
else:
    aumento = salario * 0.10
    atualsalario = aumento + salario
    print('O seu aumento será de R${:.2f}. Passano a ser R${:.2F}.'.format(aumento, atualsalario))
