matrix = [], [], []
for v in range(0, 9):
    if v <= 2:
        matrix[0].append(int(input(f'Digite um valor para [0, {v}]: ')))
    elif 5 >= v >= 3:
        matrix[1].append(int(input(f'Digite um valor para [1, {v - 3}]: ')))
    else:
        matrix[2].append(int(input(f'Digite um valor para [2, {v - 6}]: ')))
print(f'{"-="*30}')
for v in range(0, 3):
    print(f'[{matrix[v][0]:^5}][{matrix[v][1]:^5}][{matrix[v][2]:^5}]')
