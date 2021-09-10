nome = str(input('Digite o seu nome: ')).strip().rstrip()
print ('Seu nome escrito com letras maiscúlas é {}.'.format(nome.upper()))
print ('Seu nome escrito com letras minúsculas é {}.'.format(nome.lower()))
div = nome.split()
int = ''.join(div)
print ('No total seu nome tem {} letras.'.format(len(int)))
pnome = div [0]
print ('Seu primeiro nome tem {} letras.'.format(len(pnome)))
