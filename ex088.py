# Sorteie números da mega sena
from random import sample
from time import sleep
jogos = list()
print('-' * 40)
print(f'{'GERADOR DE NÚMEROS - MEGA SENA':^40}')
print('-' * 40)
num = int(input('Quantos jogos você deseja sortear? '))
print(f'{'=-' * 5} SORTEANDO {num} JOGOS {'-=' * 5}')
for j in range (num):
    sorteio = sample(range(1,61), 6)
    sorteio.sort()
    jogos.append(sorteio[:])
    print(f'Jogo {j + 1}: {jogos[j]}')
    sleep(1)
print('=' * 40)
