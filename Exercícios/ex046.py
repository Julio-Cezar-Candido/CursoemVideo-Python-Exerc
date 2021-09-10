from time import sleep
from emojis import encode
print('CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFÍCIOS:')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(encode(':fireworks:FELIZ ANO NOVO!!!:fireworks:'))
