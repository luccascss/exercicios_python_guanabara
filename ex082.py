# colocar vários valores numa lista e posteriormente criar outras 2 listas com valores pares e ímpares
contador = 0
lista_num = list()
lista_par = list()
lista_impar = list()
resp = ''
while True:
    contador = contador + 1
    lista_num.append(int(input(f'Digite o {contador}° valor: ')))
    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resp != 'S' and resp != 'N':
            print('Escolha [ S ] para sim')
            print('Escolha [ N ] para não')
    if resp == 'S':
        resp = ''
    else:
        break
print(f'Valores digitados: {lista_num}')
for n in lista_num:
    if n % 2 == 0:
        lista_par.append(n)
    elif n % 2 != 0:
        lista_impar.append(n)
print(f'Lista de valores pares: {lista_par}')
print(f'Lista de valores ímpares: {lista_impar}')