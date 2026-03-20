# crie um função chamada voto() que receba o parâmetro ano de nascimento e retorne um valor literal indicando: voto negado, voto opcional ou voto obrigatório.
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 120 >= idade >= 65 or idade == 16 or idade == 17:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif 16 > idade >= 0:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 65 > idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return 'Valores inválidos.'

ano_nasc = int(input('Em que ano você nasceu? '))
print(voto(ano_nasc))


