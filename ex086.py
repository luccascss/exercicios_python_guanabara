# crie uma matriz 3x3 e depois mostre-a na tela com a formatação correta
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for p in range(0, 3):
        matriz[l][p] = int(input(f'Digite o valor para [{l}, {p}]: '))
for l in range(0, 3):
    for p in range(0, 3):
        print(f'[{matriz[l][p]:^5}]', end='')
    print()
