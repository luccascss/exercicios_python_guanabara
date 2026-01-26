# número primo ou não
num = int(input('Digite um número inteiro: '))
soma = 0
for n in range(2, num + 1):
    if num % n == 0:
        soma += 1
    else:
        soma += 0
print('O número {} foi divisível {}x'.format(num, soma))
if soma == 1:
    print('O número {} é primo!'.format(num))
else:
    print('O número {} não é primo!'.format(num))
