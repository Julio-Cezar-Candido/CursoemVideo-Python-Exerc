cidade = str(input('Digite o nome de uma cidade: '))
nm = cidade.strip().rstrip().upper()
div = nm.split()
pome = div [0]
print ('É {} a afirmção que sua cidade começa com SANTO'.format('SANTO' in pome))