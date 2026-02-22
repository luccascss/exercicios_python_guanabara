# Leia nome, ano de nascimento e CTPS e cadastre os dados (com idade) num dicionário. Caso CTPS seja diferente de zero, calcule quanto tempo falta para o indivíduo se aposentar.
from datetime import date
ano_atual = date.today().year
dados_individuo = dict()
dados_individuo['nome'] = str(input('Nome: ')).strip().upper()
dados_individuo['idade'] = ano_atual - int(input('Ano de nascimento: '))
dados_individuo['ctps'] = int(input('N° CTPS: [0 caso nao tenha] '))
if dados_individuo['ctps'] != 0:
    dados_individuo['contratacao'] = int(input('Ano da contratação: '))
    dados_individuo['salario'] = float(input('Salário: R$ '))
    tempo_cont = (ano_atual - dados_individuo['contratacao'])
    tempo_cont_rest = (35 - tempo_cont) + dados_individuo['idade']
    dados_individuo['aposentadoria'] = tempo_cont_rest
print(dados_individuo)
for k, v in dados_individuo.items():
    print(f'{k} tem o valor de {v}')
