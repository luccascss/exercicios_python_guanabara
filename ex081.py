#coloque números numa lista e diga quantos valores foram digitados, mostra a lista em ordem decrescente e diga se o n° 5 foi digitado ou não
contador = 0
lista_num = []
resposta = ''
while True:
    contador = contador + 1
    lista_num.append(int(input(f'Digite o {contador}° número: ')))
    while resposta != 'N' and resposta != 'S':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resposta not in 'SN':
            print('Escolha [ S ] para sim')
            print('Escolha [ N ] para não')
    if resposta == 'N':
        break
    else:
        resposta = ''
# número de elementos da lista:
print(f'Foram digitados {len(lista_num)} números.')
# valores da lista em ordem decrescente:
lista_num.sort(reverse=True)
print(f'Valores da lista em ordem DECRESCENTE: {lista_num}')
# presença do n° 5:
if 5 not in lista_num:
    print('O número 5 não se encontra na lista')
else:
    print('O número 5 aparece nas posições: ', end='')
    for p, n in enumerate(lista_num):
        if 5 == n:
            print(f'{p} ... ', end='')
