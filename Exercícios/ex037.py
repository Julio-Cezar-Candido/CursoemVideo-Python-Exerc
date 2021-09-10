valor = int(input('Digite um número inteiro: '))
print('Escolha uma da opções abaixo para converter esse numero em:')
convert = int(input('[1] BINÁRIO\n'
                    '[2] OCTAL\n'
                    '[3] HEXADECIMAL\n'
                    '       \n'
                    'Opção: '))
if convert == 1:
    print('O número {} em BINÁRIO é igual a: {}'.format(valor, bin(valor)[2:]))
elif convert == 2:
    print('O número {} em OCTAL é igual a: {}'.format(valor, oct(valor)[2:]))
elif convert == 3:
    print('O número {} em HEXADECIMAL é igual a: {}'.format(valor, hex(valor)[2:]))
else:
    print('A opção INVALIDA! Tente novamente.')
