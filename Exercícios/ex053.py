frase = str(input('Digite uma frase: ')).strip().upper()
separa = frase.split()
junto = ''.join(frase)
inverso = junto[::-1]
#inverso = ''
#for letra in range(len(junto) -1, -1, -1):
#    inverso += junto[letra]
print('A frase "{}" lida de trás para frente fica: "{}".'.format(frase, inverso))
if inverso == junto:
    print('Portanto a frase digitada é um PALÍNDROME!')
else:
    print('Portanto a frase digitada NÃO é um PALÍDROMO!')
