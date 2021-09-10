def leiaInt(perguta):
    '''numero = str(input(perguta)).strip()
    while not numero.isnumeric():
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        numero = input(perguta).strip()'''
    ok = False
    numero = 0
    while True:
        numero = str(input(perguta)).strip()
        if numero.isnumeric():
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return numero


#Programa principal
print(f'{"-*"*11}')
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
