# crie uma matriz 3x3 e depois mostre-a na tela com a formatação correta
matriz = [[], [], [], [], [], [], [], [], []]
for c in range(0, 9):
    valor = int(input(f'Digite o {c + 1}° valor: '))
    matriz[c].append(valor)
print(f'{matriz[0]}{matriz[1]}{matriz[2]}')
print(f'{matriz[3]}{matriz[4]}{matriz[5]}')
print(f'{matriz[6]}{matriz[7]}{matriz[8]}')
