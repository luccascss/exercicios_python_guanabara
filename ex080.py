#coloque 5 valores em uma lista em ordem crescente sem utilizar o método sort
lista_num = list()
for _ in range (5):
    num = (int(input('Digite um valor: ')))
    for n in lista_num:
        if num >= n:
            lista_num.append(num)
            print('Valor adicionado ao final da lista...')
        elif num < n:
            lista_num.insert(0, num)
            print('Valor adicionado na posição 0 da lista...')
print(lista_num)