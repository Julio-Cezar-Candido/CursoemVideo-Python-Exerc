jogadores = []
while True:
    print('-'*30)
    jogador = {'nome': str(input('Nome do jogador: ')).strip()}
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    for p in range(1, partidas + 1):
        gols.append(int(input(f'   Quantos na partida {p}? ')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    jogador.clear()
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'NS':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if r == 'N':
        break
print(f'{"-="*30}\n{"cod":<4}{"nome":<12}{"gols":<20}{"total":>5}\n{"-"*42}')
for pos, jo in enumerate(jogadores):
    print(f'{pos:>3} {jo["nome"]:<12}{str(jo["gols"]):<20}{jo["total"]:>5}')
while True:
    print('-' * 42)
    r = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if r == 999:
        print(' <ENCERRANDO>')
        break
    if r >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {r}!')
    elif r < 0:
        print(f'ERRO! Não existe jogador com código {r}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[r]["nome"]}:')
        for n in range(0, len(jogadores[r]['gols'])):
            print(f'No {n+1}º jogo o {jogadores[r]["nome"]} fez {jogadores[r]["gols"][n]}.')
print('Volte sempre!')