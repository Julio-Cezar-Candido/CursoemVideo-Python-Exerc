from random import randint
from time import sleep
print(f'{"-"*60}\nVou pensar em um número entre 0 e 5. Tente adivinhar...'
      f'\n{"-"*60}\nPROCESSANDO.....')
sleep(3)
while True:
    computador = randint (0, 5) #Faz o computador pensar
    jogador = int(input('Em qual número pensei? ')) #Jogador adiviando
    while jogador not in (1, 2, 3, 4, 5):
        print('Opção INVÁLIDA!'
              'Tente novamente')
        jogador = float(input('Em qual número pensei? '))  # Jogador adiviando
    else:
        if computador == jogador:
            perg = str(input('!Você GANHOU! PARABÉNS!!!\nVamos novamente? [S/N] ')).upper()[0]
            if perg == 'N':
                break
        else:
            perg = str(input(f'!Você PERDEU! Eu pensei no número {computador}'
                             f'\nVamos novamente? [S/N] ')).upper()[0]
            if perg == 'N':
                break
print('Volte sempre!!!')
