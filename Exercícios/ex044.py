print('{}LOJAS J.C.SILVA{}'.format('='*16, '='*16))
preço = float(input('Preço das compras: R$'))
pag = int(input('FORMAS DE PAGAMENTO\n'
                '[1] A vista no dinheiro ou cheque\n'
                '[2] A vista no cartão de débito\n'
                '[3] 2x no cartão\n'
                '[4] de 3x até 12x no cartão\n'
                'Qual é a opção? '))
if pag == 1:
    print('Você terá 10% de deconto, e pagará apenas R${:.2f} pelas suas compras.'.format(preço*0.9))
elif pag == 2:
    print('Você terá 10% de deconto, e pagará apenas R${:.2f} pelas suas compras.'.format(preço*0.95))
elif pag == 3:
    print('Você pagará o preço normal de R${:.2f} e '
          'R${:.2f} será o preço da suas parcelas.'.format(preço, preço/2))
elif pag == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Seu produto terá um acrescimo de 20%.\n'
          'Passando de R${:.2f} para R${:.2f} pelas suas compras.\n'
          'Sendo R${:.2f} o valor de cada parcela.'.format(preço, ((preço*0.2)+preço), ((preço*0.2)+preço)/parcelas))
else:
    print('Opção INVALIDA! Tente novamente')
