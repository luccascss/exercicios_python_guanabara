# Leia vários inputs com nome e peso guardando numa lista. Depois, diga quantas pessoas foram cadastradas, quais as mais pesadas e quais a mais leves
dados = list()
lista_dados = list()
resposta = ''
cont_pessoas = 0
lista_pessoas = list()
lista_peso = list()
nome_peso_maior = list()
nome_peso_menor = list()
while True:
    nome = str(input('Nome: ')).strip().upper()
    peso = float(input('Peso: [Kg] '))
    if peso < 0:
        print('Idade digitada inválida.')
    else:
        dados.append(nome)
        dados.append(peso)
        lista_dados.append(dados[:])
        dados.clear()
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resposta != 'S' and resposta != 'N':
            print('Escolha [ S ] para sim')
            print('Escolha [ N ] para não')
    if resposta == 'S':
        resposta = ''
    elif resposta == 'N':
        break
for e, p in enumerate(lista_dados):
    cont_pessoas += 1
    lista_pessoas.append(lista_dados[e][0])
    lista_peso.append(lista_dados[e][1])
for e, p in enumerate(lista_dados):
    if max(lista_peso) == lista_dados[e][1]:
        nome_peso_maior.append(lista_dados[e][0])
    elif min(lista_peso) == lista_dados[e][1]:
        nome_peso_menor.append(lista_dados[e][0])
print(f'Foram cadastradas {cont_pessoas} pessoas: {lista_pessoas}')
print(f'Maior peso foi de {max(lista_peso)}: {nome_peso_maior}')
print(f'Menor peso foi de {min(lista_peso)}: {nome_peso_menor}')
