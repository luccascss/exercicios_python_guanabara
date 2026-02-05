#gerar 5 números aleatórios e armazenar em tupla, informando o maior e menor valor
from random import randint
numeros = tuple(randint(1,10) for _ in range(5))
#usar " _ " quando o valor de for não for relevante para o código
print(f'Os valores sorteados foram: {numeros}')
print(f'O maior valor foi: {max(numeros)}')
print(f'O menor valor foi: {min(numeros)}')