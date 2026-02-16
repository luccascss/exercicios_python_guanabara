# Leia vários inputs com nome e peso guardando numa lista. Depois, diga quantas pessoas foram cadastradas, quais as mais pesadas e quais a mais leves
dados_temp = list()
dados = list()
resposta = ''
maior_peso = 0
menor_peso = 0
pessoas = list()
nome_peso_maior = list()
nome_peso_menor = list()
while True:
    nome = str(input('Nome: ')).strip().upper()
    peso = float(input('Peso: [Kg] '))
    if peso < 0:
        print('Peso digitado inválido.')
    else:
        dados_temp.append(nome)
        dados_temp.append(peso)
        if len(dados) == 0:
            maior_peso = peso
            menor_peso = peso
        else:
            if peso > maior_peso:
                maior_peso = peso
            elif peso < menor_peso:
                menor_peso = peso
        dados.append(dados_temp[:])
        dados_temp.clear()
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resposta != 'S' and resposta != 'N':
            print('Escolha [ S ] para sim')
            print('Escolha [ N ] para não')
    if resposta == 'S':
        resposta = ''
    elif resposta == 'N':
        break
for p in dados:
    pessoas.append(p[0])
    if maior_peso == p[1]:
        nome_peso_maior.append(p[0])
    if menor_peso == p[1]:
        nome_peso_menor.append(p[0])
print(f'Foram cadastradas {len(pessoas)} pessoas: {pessoas}')
print(f'Maior peso foi de {maior_peso}Kg: {nome_peso_maior}')
print(f'Menor peso foi de {menor_peso}Kg: {nome_peso_menor}')
