# Add nome, sexo, idade de várias pessoas num dicionário e posteriormente dentro de uma lista. No final, mostre quantas pessoas foram cadastradas, média de idade de todas as pessoas, lista com todas as mulheres e lista com todas as pessoas com idade acima da média.
cont = ''
dados_temp = dict()
lista_pessoas = list()
soma_idade = 0
lista_mulheres = list()
lista_idade_media = list()
while True:
    dados_temp['nome'] = str(input('Nome: ')).strip().upper()
    # validação de sexo
    while True:
        dados_temp['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()
        if dados_temp['sexo'] != 'F' and dados_temp['sexo'] != 'M':
            print('Opção inválida.')
        else:
            break
    #validação de idade
    while True:
        dados_temp['idade'] = int(input('Idade: '))
        if dados_temp['idade'] < 0 or dados_temp['idade'] > 120:
            print('Idade inválida.')
        else:
            break
    lista_pessoas.append(dados_temp.copy()) #add cópia do dicionário na lista principal
    dados_temp.clear() # limpa dicionário para reutilização
    #validação de continuação
    while True:
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if cont != 'S' and cont != 'N':
            print('Opção inválida.')
        if cont in 'SN':
            break
    if cont == 'S':
        cont = ''
    else:
        break

print(f'Foram cadastradas {len(lista_pessoas)} pessoas.')
# loop para destrinçar a lista e acessar os dicionários individualmente
for d in lista_pessoas:
    soma_idade = soma_idade + d['idade']
    if d['sexo'] == 'F':
        lista_mulheres.append(d['nome'])

media_idade = soma_idade / len(lista_pessoas)

# loop para destrinçar a lista e acessar os dicionários individualmente
for d in lista_pessoas:
    if d['idade'] > media_idade:
        lista_idade_media.append(d['nome'][:])

print(f'A média de idade do grupo é de {media_idade:.1f}')
print(f'As mulheres são: {lista_mulheres}')
print(f'Pessoas com idade acima da média ({media_idade}): {lista_idade_media}')
