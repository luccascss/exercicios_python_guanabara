#Fatorial usando if
resultado = 1
num = int(input('Digite um número inteiro para calcular seu fatorial: '))
if num < 0:
    while num <0:
        num = int(input('Tente novamente com um número válido: '))
print(f'O resultado é: ')
print(f'{num}! = ', end='')
for fatorial in range(num, 0, -1):
    resultado = resultado * fatorial
    print(f'{fatorial}', end='')
    print(' x ' if fatorial > 1 else ' = ', end='')
print(f'{resultado}')
