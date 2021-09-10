n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
     'nove', 'dez', 'oze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
     'dezesete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while 0 > num or num > 20:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {n[num]}.')
