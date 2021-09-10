from time import sleep
opcao = 0
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
while opcao != 5:
    opcao = int(input('{}\nSelecine uma das opção:\n'
                      ' [1] Somar\n'
                      ' [2] Multiplicar\n'
                      ' [3] Maior\n'
                      ' [4] Novos números\n'
                      ' [5] Sair do programa\n{}\n'
                      '>>> Opção desejada: '.format('=-='*8, '=-='*8)))
    if opcao == 1:
        print('A soma entre {:.2f} e {:.2f} é igual a {:.2f}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação entre {:.2f} e {:.2f} é igual a {:.2f}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 - n2 == 0:
            maior = 'nenhum, pois ambos são iguais'
        elif n1 - n2 < 0:
            maior = n2
        elif n1 - n2 > 0:
            maior = n1
        print('O maior número entre {:.2f} e {:.2f} é igual a {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('FINALIZANDO...\n{}'.format('='*15))
    else:
        print('Opção INVÁLIDA!!! Tente novamente!')
sleep(2)
print('Volte sempre!')
