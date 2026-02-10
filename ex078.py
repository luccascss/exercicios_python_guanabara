#guarde inputs numa lista e no final mostre o maior e o menor
valores = list()
for p in range(5):
    valores.append(int(input(f'Digite um número para a posição {p}: ')))
valor_max = max(valores)
valor_min = min(valores)
print(f'Lista com os valores: {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ',end='')
for e, v in enumerate(valores):
    if valor_max == v:
        print(f'{e}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ',end='')
for e, v in enumerate(valores):
    if valor_min == v:
        print(f'{e}... ', end='')

