print('{}\n SEQUÊNCIA DE FIBONACCI\n{}'.format('-=*'*10,'-=*'*10))
n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
t3 = t1 + t2
print('-'*30)
print('{} > {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t2 = t1
    t1 = t3
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    cont += 1
print(' > FIM!')
print('-'*30)
