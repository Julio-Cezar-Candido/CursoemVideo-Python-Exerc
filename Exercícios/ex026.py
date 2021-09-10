frase = str(input('Digite uma frase:'))
fm = frase.strip().rstrip().upper()
qa = fm.count('A')
oiA = fm.find('A')+1
otA = fm.rfind('A')+1
print ('Na sua frase aparece {} vezes a letra A.\nOnde o primeiro A inicia-se na {} posição.\n'
       'O último A termina na posição {}.'.format(qa, oiA, otA))
