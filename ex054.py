#maioridade
from datetime import date
lista = []
lista_menor = []
lista_maior = []
for a in range (1, 4 + 1):
    idade = int(input('Digite seu ano de nascimento: '))
    lista.append(idade)
print('As idades digitadas foram: {}'.format(lista))
for i in lista:
    ano = (date.today().year - i)
    total = 0
    if ano >= 21:
        lista_maior.append(i)
    else:
        lista_menor.append(i)
print('Ao todo {} pessoas são menores de idade e {} pessoas são maiores de idade'.format(len(lista_menor), len(lista_maior)))
