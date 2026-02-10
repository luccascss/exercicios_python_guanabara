#guarde inputs numa lista e no final mostre o maior e o menor
valores = list()
for p in range(5):
    valores.append(int(input(f'Digite um número para a posição {p}: ')))
print(f'Lista com os valores: {valores}')
print(f'O maior valor digitado foi {max(valores)} e sua posição na lista é {valores.index(max(valores))}')
print(f'O menor valor digitado foi {min(valores)} e sua posição na lista é {valores.index(min(valores))}')
