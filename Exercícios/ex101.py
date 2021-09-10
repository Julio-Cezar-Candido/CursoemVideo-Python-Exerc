def voto(ano_nascimento):
    from datetime import date
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 18 > idade >= 16 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


#PROGRAMA PRINCIPAL
print('-' * 30)
#nasc = int(input('Em que ano você nasceu? '))
print(voto(int(input('Em que ano você nasceu? '))))
