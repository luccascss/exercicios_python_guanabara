# Adicionando valores de um dado num dicionário e os colocando em ordem crescente
from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
ranking = dict()
for j in range (1, 5):
    jogo[f'jogador_{j}'] = randint(1,6)
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'   O {k} tirou {v}')
    sleep(1)
print('Ranking dos Jogadores: ')
ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)
for i, (k, v) in enumerate(ranking):
    print(f'   {i + 1}° lugar: {k} com {v}')
