nome = str(input('Digite seu nome: '))
nomet = nome.strip().rstrip().upper()
nomed = nomet.split()
pnome = nomed [0]
unome = nomed [-1]
print ('Seu primeiro nome é: {}. E o último nome é: {}.'.format(pnome, unome))
