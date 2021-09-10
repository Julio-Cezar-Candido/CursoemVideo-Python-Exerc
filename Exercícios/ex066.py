cont = soma = 0
while True:
    nun = int(input('Digite um valor (999 para parar): '))
    if nun == 999:
        break
    soma += nun
    cont += 1
print(f'A soma dos {cont} números foi {soma}!')
