from random import randint
from time import sleep
computador = randint (0, 10) #Faz o computador pensar
print ('------' * 9)
print ('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print ('------' * 9)
print ('PROCESSANDO.....')
sleep(3)
jogador = 11
cot = 0
while jogador != computador:
    jogador = int(input('Em qual número eu pensei? '))
    cot += 1
    if jogador > computador:
        print('Menos... Tente novamente!')
    elif jogador < computador:
        print('Mais... Tente novamente!')
print('Você ACERTOU!!! Parabéns!!!\nFoi necessário {} tentativas!'.format(cot))
