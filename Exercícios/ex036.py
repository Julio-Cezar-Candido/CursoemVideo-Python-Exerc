casa = float(input('\033[0;33mQual é o valor da casa? R$'))
salario = float(input('Qual é o seu sálario, mensal atual? R$'))
anos = int(input('Em quantos anos você pretende pagar a casa? '))
prestação = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.{}'
      .format(casa, anos, prestação, '\033[m'))
if prestação <= salario * 0.30:
    print('{}Parabéns!!! Seu emprestimo foi{}{} APROVADO!!!!{}'.format('\033[36m', '\033[m', '\033[34m', '\033[m'))
else:
    print('\033[31mInfelimesnte seu emprestimo foi NEGADO'
          '\nPois a prestação  ultrapassou 30% do seu salário de R${:.2f}.\033[m'
          .format(prestação, salario))
