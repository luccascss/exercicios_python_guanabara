# aprimore o desafio 086 mostrando no final: a soma de todos os valores pares, soma dos valores da terceira coluna, maior valor da segunda linha
soma_par = 0
soma_coluna = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for p in range(0, 3):
        matriz[l][p] = int(input(f'Digite o valor para [{l}, {p}]: '))
for l in range(0, 3):
    for p in range(0, 3):
        print(f'[{matriz[l][p]:^5}]', end='')
    print()
for listas in matriz:
    soma_coluna = soma_coluna + listas[2]
    for n in listas:
        if n % 2 == 0:
            soma_par = soma_par + n
print(f'A soma dos valores pares digitados é de: {soma_par}')
print(f'A soma dos valores da terceira coluna é de: {soma_coluna}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')