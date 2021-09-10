n = soma = cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        cont += 1
print('Foi digitado {} números.\nE a soma entre eles foi de {}.'.format(cont, soma))
