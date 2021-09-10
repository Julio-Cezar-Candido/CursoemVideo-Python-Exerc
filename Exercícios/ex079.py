valores = [int(input('Digite um valor: '))]
print('Valor adicionado com sucesso...')
while True:
    continuar = str(input('Quer continuar? ')).strip().upper()[0]
    if continuar == 'S':
        valor = int(input('Digite um valor: '))
        if valor not in valores:
            valores.append(valor)
            print('Valor adicionado com sucesso...')
        else:
            print('Valor Duplicado! Não irei adicionar!')
    elif continuar == 'N':
        break
print(f'{"-="*32}\nVocê digitou os valores {sorted(valores)}')
