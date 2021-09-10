from datetime import date
atual = date.today().year
nasc = int(input('Qual é o ano do seu nascimento? '))
idade = atual - nasc
if idade == 18:
    print('Você já tem ou vai fazer 18 anos.\n'
          'Você já pode se apresentar para o alistamento obrigatório.\n'
          'SIRVA BEM AO SEU PAÍS!!!!!!!!!!!!')
elif idade < 18:
    print('Você só tem {} anos ou vai fazer este ano.\n'
          'Ainda falta {} anos para você se apresentar para o alistamento obrigatório.\n'
          'Admiramos sua ansiedade!!! Nós vemos em {} anos.'.format(idade, 18 - idade, ((18 - idade) + nasc + idade)))
else:
    print('SEU VAGABUNDO!!!! Já passaram {} anos do seu alistamento obrigatório!!!!\n'
          'Afinal vc já tem {} anos ou ainda vai fazer este ano.\n'
          'Você é uma vergonha para sua nação!!!'.format(idade - 18, idade))
