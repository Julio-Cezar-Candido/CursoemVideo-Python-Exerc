tabuada = 0
while True:
    tabuada = int(input(f'{"-"*35}\n Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        break
    print(f'{"-"*35}')
    for c in range(1, 11):
        print(f'{tabuada} x {c} = {c * tabuada}')
print(f'{"-"*35}\nPROGRAMA TABUADA ENCERRADO. Volte sempre!')
