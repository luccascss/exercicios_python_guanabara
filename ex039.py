# serviço de alistamento
from datetime import date
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
print('''Escolha "F" para Feminino: 
Escolha "M" para Masculino:''')
sexo = str(input('Digite sua escolha: ')).strip().upper()
data_atual = date.today().year
idade_ano_atual = (data_atual - ano_nascimento)
ano_18 = (ano_nascimento + 18)
if idade_ano_atual <= 0 or ano_nascimento < 1910:
    input('Insira um número válido.')
elif sexo != "F" and sexo != "M":
    print('Insira uma opção de sexo válida.')
elif sexo == "F":
    print('Você não precisa realizar o alistamento obrigatório!')
elif idade_ano_atual < 18 and sexo == "M":
    print('Você precisará se alistar daqui {} anos'.format(18 - idade_ano_atual))
    print('Você fará 18 anos em {}'.format(ano_18))
elif idade_ano_atual == 18 and sexo == "M":
    print('Procure a Junta de Serviço Militar e realize o alistamento obrigatório!')
elif idade_ano_atual > 18 and sexo == "M":
    idade_atual = (data_atual - ano_nascimento)
    print('Você deveria ter realizado o alistamento obrigatório há {} anos'.format(idade_ano_atual - 18))
    print('Você vai fazer em {}, {} anos.'.format(data_atual, idade_atual))


