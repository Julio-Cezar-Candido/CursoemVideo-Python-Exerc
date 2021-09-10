from random import choice
from time import sleep
import emojis
comp = choice(['pedra', 'papel', 'tesoura'])
print('-----' * 8)
print('VAMOS JOGAR PEDRA, PAPEL E TESOURA...')
print('-----' * 8)
jogador = int(input(emojis.encode('Escolha uma das opções:\n'
                                  '[1] PEDRA :punch:\n'
                                  '[2] PAPEL :hand:\n'
                                  '[3] TESOURA :scissors:\n'
                                  'Opção: ')))
if comp == 'pedra' and jogador == 1:
    print('JO')
    sleep(1)
    print('KE')
    sleep(1)
    print('PO!!!!')
    sleep(1)
    print(emojis.encode(':punch: X :punch:'))
    print(emojis.encode('EMPATAMOS :sweat_smile:\n'
                        'VAMOS JOGAR DE NOVO! :smile:'))
elif comp == 'pedra' and jogador == 2:
    print('JO')
    sleep(1)
    print('KE')
    sleep(1)
    print('PO!!!!')
    sleep(1)
    print(emojis.encode(':punch: X :hand:'))
    print(emojis.encode('VOCÊ GANHOU!!!\n'
                        'PARABÉNS :clap:\n'
                        'VAMOS JOGAR DE NOVO! :smile:'))
elif comp == 'pedra' and jogador == 3:
    print('JO')
    sleep(1)
    print('KE')
    sleep(1)
    print('PO!!!!')
    sleep(1)
    print(emojis.encode(':punch: X :scissors:'))
    print(emojis.encode('VOCÊ PERDEU!!! :joy:\n'
                        'VAMOS JOGAR DE NOVO! :smile:'))
elif comp == 'papel' and jogador == 1:
    print('JO')
    sleep(1)
    print('KE')
    sleep(1)
    print('PO!!!!')
    sleep(1)
    print(emojis.encode(':hand: X :punch:'))
    print(emojis.encode('VOCÊ PERDEU!!! :joy:\n'
                        'VAMOS JOGAR DE NOVO! :smile:'))
elif comp == 'papel' and jogador == 2:
    print('JO')
    sleep(1)
    print('KE')
    sleep(1)
    print('PO!!!!')
    sleep(1)
    print(emojis.encode(':hand: X :hand:'))
    print(emojis.encode('EMPATAMOS :sweat_smile:\n'
                        'VAMOS JOGAR DE NOVO! :smile:'))
elif comp == 'papel' and jogador == 3:
    print('JO')
    sleep(1)
    print('KE')
    sleep(1)
    print('PO!!!!')
    sleep(1)
    print(emojis.encode(':punch: X :scissors:'))
    print(emojis.encode('VOCÊ GANHOU!!!\n'
                        'PARABÉNS :clap:\n'
                        'VAMOS JOGAR DE NOVO! :smile:'))
elif comp == 'tesoura' and jogador == 1:
    print('JO')
    sleep(1)
    print('KE')
    sleep(1)
    print('PO!!!!')
    sleep(1)
    print(emojis.encode(":scissors: X :punch:"))
    print(emojis.encode('VOCÊ GANHOU!!!\n'
                        'PARABÉNS :clap:\n'
                        'VAMOS JOGAR DE NOVO! :smile:'))
elif comp == 'tesoura' and jogador == 2:
    print('JO')
    sleep(1)
    print('KE')
    sleep(1)
    print('PO!!!!')
    sleep(1)
    print(emojis.encode(':scissors: X :hand:'))
    print(emojis.encode('VOCÊ PERDEU!!! :joy:\n'
                        'VAMOS JOGAR DE NOVO! :smile:'))
elif comp == 'tesoura' and jogador == 3:
    print('JO')
    sleep(1)
    print('KE')
    sleep(1)
    print('PO!!!!')
    sleep(1)
    print(emojis.encode(':scissors: X :scissors:'))
    print(emojis.encode('EMPATAMOS :sweat_smile:\n'
                        'VAMOS JOGAR DE NOVO! :smile:'))
else:
    print('Opção INVALIDA! Tente novamente')
