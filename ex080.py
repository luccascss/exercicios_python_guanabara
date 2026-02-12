#coloque 5 valores em uma lista em ordem crescente sem utilizar o método sort
lista_num = list()
for c in range(5):
    num = (int(input(f'Digite o {c + 1}° valor: ')))
    if c == 0 or num > lista_num[-1]:
        lista_num.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista_num):
            if num <= lista_num[pos]:
                lista_num.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos = pos + 1
print(lista_num)
