num = int(input('Digite um número inteiro e saiba se ele é par ou ímpar: '))
resultado = (num % 2)
if resultado == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é ímpar!'.format(num))
print('------FIM------')

