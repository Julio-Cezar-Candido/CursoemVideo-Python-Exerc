matrix = [[], [], []]
maior2 = soma3 = somapares = 0
for v in range(0, 9):
    if v <= 2:
        matrix[0].append(int(input(f'Digite um valor para [0, {v}]: ')))
        if matrix[0][len(matrix[0])-1] % 2 == 0:
            somapares += matrix[0][len(matrix[0])-1]
        if len(matrix[0]) == 3:
            soma3 += matrix[0][2]
    elif 5 >= v >= 3:
        matrix[1].append(int(input(f'Digite um valor para [1, {v - 3}]: ')))
        if matrix[1][len(matrix[1])-1] % 2 == 0:
            somapares += matrix[1][len(matrix[1])-1]
        if len(matrix[1]) == 1:
            maior2 = matrix[1][0]
        elif len(matrix[1]) == 2:
            if matrix[1][len(matrix[1])-1] > maior2:
                maior2 = matrix[1][len(matrix[1])-1]
        else:
            soma3 += matrix[1][2]
            if matrix[1][len(matrix[1])-1] > maior2:
                maior2 = matrix[1][len(matrix[1])-1]
    else:
        matrix[2].append(int(input(f'Digite um valor para [1, {v - 6}]: ')))
        if matrix[2][len(matrix[2])-1] % 2 == 0:
            somapares += matrix[2][len(matrix[2])-1]
        if len(matrix[2]) == 3:
            soma3 += matrix[2][2]
print(f'{"-="*25}')
for v in range(0, 3):
    print(f'[{matrix[v][0]:^5}][{matrix[v][1]:^5}][{matrix[v][2]:^5}]')
print(f'{"-="*25}\nA soma dos valores pares é {somapares}.\n'
      f'A soma dos valores da terceira coluna é {soma3}.\n'
      f'O maior valor da segunda linha é {maior2}.')
