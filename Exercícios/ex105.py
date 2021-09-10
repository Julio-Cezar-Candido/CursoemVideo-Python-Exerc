def notas(* n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcinal, indicando se deve ou não adicinar a situação
    :return: dicinário com várias informações sobre a situação da turma.0
    '''
    '''cont = maior = menor = soma = 0
    for c in n:
        cont += 1
        soma += c
        if cont == 1:
            maior = c
            menor = c
        else:
            if maior < c:
                maior = c
            if menor > c:
                menor = c
    media = soma/cont
    avaliação = {'total': cont, 'maior': maior, 'menor': menor, 'média': media}'''
    avaliação = dict()
    avaliação['Total'] = len(n)
    avaliação['Maior'] = max(n)
    avaliação['Menor'] = min(n)
    avaliação['Média'] = sum(n)/len(n)
    if sit == True:
        if avaliação['Média'] < 5:
            avaliação['situação'] = 'RUIM'
        elif 5 <= avaliação['Média'] < 7:
            avaliação['situação'] = 'RAZOÁVEL'
        elif avaliação['Média'] >= 7:
            avaliação['situação'] = 'BOA'
    return avaliação


#Programa principal
resp = notas(6, 6, sit=True)
print(resp)
