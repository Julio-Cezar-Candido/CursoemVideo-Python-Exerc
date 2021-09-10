from time import sleep


def maior(* n):
    print(f'{"-=" *   15}\nAnalisando os valores passados...')
    cont = mai = 0
    for c in n:
        print(c, end=' ')
        sleep(0.5)
        cont += 1
        if cont == 1:
            mai = c
        else:
            if mai < c:
                mai = c
    print(f'Foram informados {cont} valores ao todo.\n'
          f'O maior valor informado foi {mai}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
