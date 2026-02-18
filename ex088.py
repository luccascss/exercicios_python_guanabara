# Sorteie números da mega sena
from random import randint
from time import sleep
jogos = list()
jogo_temp = list()
print('-' * 40)
print(f'{'GERADOR DE NÚMEROS - MEGA SENA':^40}')
print('-' * 40)
num = int(input('Quantos jogos você deseja sortear? '))
print(f'{'=-' * 5} SORTEANDO {num} JOGOS {'-=' * 5}')
for j in range (num):
    for n in range (6):
        sorteio = randint(1, 60)
        jogo_temp.append(sorteio)
    jogo_temp.sort()
    jogos.append(jogo_temp[:])
    jogo_temp.clear()
    print(f'Jogo {j + 1}: {jogos[j]}')
    sleep(1)
print('=' * 40)

