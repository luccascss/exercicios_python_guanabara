#sequência de Fibonacci
print('Descubra a sequência de Fibonacci: ')
num = int(input('Quantos elementos da sequência deseja ver? '))
f_zero = 0
f_um = 1
f = 0
contador = 1
total = 0
while num != 0:
    if num > 0:
        total = total + num
        while contador <= total:
            contador = contador + 1
            f = f_zero + f_um
            if contador <= total:
                print(f'{f} > ', end='')
            else:
                print(f'{f} > ', end='')
                print('PAUSA')
            f_zero = f_um
            f_um = f
        num = int(input('Quantos elementos da sequência deseja ver? '))
    if num == 0:
        print('Finalizando...')
    elif num < 0:
        num = int(input('Digite um valor válido: '))
print(f'O programa foi finalizado com {total} números da Sequência de Fibonacci demostrados!')

