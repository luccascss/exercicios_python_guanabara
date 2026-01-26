#análise de maioridade considerando o ano de nascimento
from datetime import date
ano_atual = date.today().year
soma_maior_idade = 0 #acumulador
soma_menor_idade = 0 #acumulador
print('Digite a seguir o ano de nascimento de SETE pessoas e descubra quantas atingiram a maioridade')
for i in range(1, 8):
    ano_nasc = int(input('{}ª pessoa: '.format(i)))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        soma_maior_idade = soma_maior_idade + 1
    else:
        soma_menor_idade = soma_menor_idade + 1
print('Das pessoas analisadas, ', end= '')
if soma_menor_idade <= 1 or soma_maior_idade <= 1:
    if soma_maior_idade == 1 or soma_maior_idade == 0:

        print('{} é maior de idade'.format(soma_maior_idade), end=" e ")
    else:
        print('{} são maiores de idade'.format(soma_maior_idade), end=" e ")
    if soma_menor_idade == 1 or soma_menor_idade == 0:
        print('{} é menor de idade'.format(soma_menor_idade))
    else:
        print('{} são menores de idade'.format(soma_menor_idade))
else:
    print('{} são maiores de idade e {} são menores de idade'.format(soma_maior_idade, soma_menor_idade))
