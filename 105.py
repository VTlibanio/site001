def notas(*n, sit=False):
    """
    → Analisa notas e situações de vários alunos.
    :param n: uma ou mais notas de alunos (aceita várias)
    :param sit: valor opcional indica se deve mostrar a situação
    :return: dicionário com várias informações sobre a situação
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'REGULAR'
        else:
            r['situação'] = 'RUIM'
    
    return r

# Programa principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
# {'total': 4, 'maior': 9, 'menor': 2.5, 'média': 6.25, 'situação': 'REGULAR'}
