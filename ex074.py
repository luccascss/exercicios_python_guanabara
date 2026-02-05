#gerar 5 números aleatórios e armazenar em tupla, informando o maior e menor valor
from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: {numeros}')
print(f'O maior valor foi: {max(numeros)}')
print(f'O menor valor foi: {min(numeros)}')