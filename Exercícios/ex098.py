from time import sleep


def contador(início, fim, passo):
    if passo < 0:
        passo = passo * -1
    elif passo == 0:
        passo = 1
    print(f'{"-=" * 20}\n'
          f'Contagem de {início} até {fim} de {passo} em {passo}')
    sleep(1)
    if início <= fim:
        for c in range(início, fim + 1, passo):
            print(c, end=' ')
            sleep(0.5)
    elif início > fim:
        for c in range(início, fim - 1, passo * -1):
            print(c, end=' ')
            sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print(f'{"-=" * 20}\nAgora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
f = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, f, pas)
