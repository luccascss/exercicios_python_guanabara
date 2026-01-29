#fatorial usando while
num = int(input('Digite um número inteiro: '))
resultado = 1
fatorial = num
while fatorial != 1:
    if num <= 0:
        num = int(input('Digite um número válido: '))
    else:
        resultado = resultado * fatorial
        fatorial = fatorial - 1
print(f'O resultado da expressão {num}! é {resultado}')
