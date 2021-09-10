n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um segundo valor: '))
n3 = float(input('Digite um terceiro valor: '))
lista = [n1, n2, n3] #Organizar os valores em lista
lista.sort() #Ordenar lista
print('O maior número é: {}.'.format(lista [2]))
print('O menor valor é: {}.'.format(lista [0]))
