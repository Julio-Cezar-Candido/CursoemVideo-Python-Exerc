num = ((int(input('Digite um número: '))),
       (int(input('Digite outro número: '))),
       (int(input('Digite mais um número: '))),
       (int(input('Digite o último númrto: '))))
print(f'Você digitou os valores {num}\n'
      f'O valor 9 apareceu {num.count(9)} vez')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}º poaição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print('O(s) valor(es) par(es) digitado(s) foi(ram): ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
