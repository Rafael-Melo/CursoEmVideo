def notas(*n, sit=False):
    """
    -=> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dic={}
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['média'] = sum(n)/dic['total']
    if sit:
        if dic['média'] < 5:
            dic['situação'] = 'Ruim'
        elif dic['média'] < 7:
            dic['situação'] = 'Razoável'
        else:
            dic['situação'] = 'Boa'
    return dic


# Programa Principal
resp = notas(4.5, 7.5, 5, 10, 8.5, sit=True)
print(resp)
help(notas)
