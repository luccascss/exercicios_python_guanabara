#fatorial usando while
num = int(input('Digite um número inteiro para calcular seu Fatorial: '))
resultado = 1
fatorial = num
if num < 0:
    while num < 0:
        num = int(input('Tente novamente com um número válido: '))
else:
    print(f'Calculando...')
    print(f'{num}! = ', end='')
    while fatorial > 0:
            print(f'{fatorial}', end='')
            print(' x ' if fatorial > 1 else ' = ', end= '')
            resultado = resultado * fatorial
            fatorial = fatorial - 1
print(f'{resultado}')
