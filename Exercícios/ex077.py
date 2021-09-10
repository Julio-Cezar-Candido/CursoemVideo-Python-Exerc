palavras = ('EU', 'AMO', 'à', 'ADELCINA',
            'GOSTO', 'DE', 'JOGAR', 'CLASH', 'OF', 'CLANS',
            'ESTOU', 'APREDENDO', 'PYTHON')
for pal in palavras:
    print(f'\nNa palara {pal.upper()} temos ', end='')
    for letra in pal:
        if letra.lower() in 'aâãáàeéèêiìíîoõôòóuúùû':
            print(letra.lower(), end=' ')
