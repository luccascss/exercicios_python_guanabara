#maior e menor peso
lista = []
for p in range(1, 5 +1):
    peso = float(input('Digite seu peso [KG]: '))
    lista.append(peso)
    peso_max = max(lista)
    peso_min = min(lista)
print('Os valores digitados foram: {}'.format(lista))
print('O maior peso é {}kg e o menor peso é {}kg'.format(peso_max, peso_min))



