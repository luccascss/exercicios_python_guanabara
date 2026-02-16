# Leia 7 valores numéricos e os coloque numa única lista que mantenha os valores pares e ímpares separadas. No fim, mostre os valores em ordem crescente.
num_lista = [[], []] # par / ímpar respectivamente
for c in range (1, 8):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0: #par
        num_lista[0].append(num)
    if num % 2 != 0: #ímpar
        num_lista[1].append(num)
num_lista[0].sort()
num_lista[1].sort()
print(f'Valores pares: {num_lista[0]}')
print(f'Valores ímpares: {num_lista[1]}')
