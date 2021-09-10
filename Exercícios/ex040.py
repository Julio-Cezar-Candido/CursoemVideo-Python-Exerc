n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2
if media < 5.0:
    print('Sua média foi {:.1f} uma nota ridiculamente baixa, está reprovado!!!!'.format(media))
elif (media >= 5.0) and (media < 7):
    print('Sua média foi {:.1f}\n'
          'Você não reprovou, mas também não passou, está de recuperação!!!!'.format(media))
elif media >= 7:
    print('Sua média foi {:.1f}\n'
          'VOCÊ FOI APROVADO.\n'
          'PARABÉNS!!!!!!!'.format(media))
