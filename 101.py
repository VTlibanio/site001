def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'a idade {idade} não te concede escolha de voto'
    elif 16 <= idade < 18 or idade > 65:
        return f'a sua idade atual te concede voto opcional'
    else:
        return f'com {idade} anos, seu voto é obrigatório.'


nasc = int(input('seu ano de nasc: '))
print(voto(nasc))

