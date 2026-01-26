# JOKENPO alternativo
from random import randint
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)
print('''Escolha [ 1 ] para PEDRA
Escolha [ 2 ] para PAPEL
Escolha [ 3 ] para TESOURA''')
jogador = int(input('Digite sua escolha: ')) - 1
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Digite um número válido e tente novamente!')
else:
    print('=' * 30)
    print('O computador escolheu {}'.format(opcoes[computador]))
    print('O Jogador escolheu {}'.format(opcoes[jogador]))
    print('=' * 30)
    if computador == 0: # computador escolhe pedra
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('VITÓRIA!')
        elif jogador == 2:
            print('DERROTA!')
        else:
            print('Digite uma opção válida!')
    elif computador == 1: # computador escolhe papel
        if jogador == 0:
            print('DERROTA!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('VITÓRIA!')
        else:
            print('Digite uma opção válida!')
    elif computador == 2: # computador escolhe tesoura
        if jogador == 0:
            print('VITÓRIA!')
        elif jogador == 1:
            print('DERROTA!')
        elif jogador == 2:
            print('EMPATE!')





