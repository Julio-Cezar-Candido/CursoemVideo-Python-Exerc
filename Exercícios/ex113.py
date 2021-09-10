def leiaInt(perguta):
    while True:
        try:
            numero = int(input(perguta))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero


def leiaFloat(perguta):
    while True:
        try:
            numero = str(input(perguta)).strip().replace(',', '.')
            numero = float(numero)
        except (TypeError, ValueError):
            print('\033[31mERRO: por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero


# Programa principal
print(f'{"-*" * 14}')
nint = leiaInt('Digite um número Inteiro: ')
nfloat = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {nint} e o real foi {nfloat}')
