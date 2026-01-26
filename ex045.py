# jogo pedra-papel-tesoura
from time import sleep
from random import choice
jogo =  ['Pedra', 'Papel', 'Tesoura']
escolha_random = choice(jogo)
input('Aperte ENTER para iniciar: ')
sleep(1)
print('Olá! eu sou o campeão mundial de JOKENPÔ desta casa em específico, muito prazer em te conhecer!')
sleep(2)
print('Imagino que você queira jogar uma partida comigo...')
sleep(2)
print('.....')
sleep(1)
print('Perfeito então!')
print('Escolha uma das opções abaixo e na sequência eu escolherei também')
sleep(2)
print('Prometo que não vou olhar a sua escolha!')
print('''Escolha [ 1 ] para pedra;
Esolha [ 2 ] para papel;
Escolha [ 3 ] para tesoura;''')
num = int(input('Digite sua escolha: ')).__abs__()
sleep(1)
print('Estou pensando.....')
sleep(2)
print('.......')
sleep(1)
print('Hummmm....')
sleep(2)
print('Eu escolho {}!'.format(escolha_random))
sleep(2)
if num > 4 or num == 0:
    print('Escolha um número válido.')
elif num == 1 and escolha_random == 'Papel':
    print('Você perdeu! Papel ganha de pedra.')
elif num == 1 and escolha_random == 'Pedra':
    print('Empate! Pedra não ganha de pedra.')
elif num == 1 and escolha_random == 'Tesoura':
    print('Você me Ganhou! Pedra ganha de tesoura.')
elif num == 2 and escolha_random == 'Papel':
    print('Empate! Papel não ganha de papel.')
elif num == 2 and escolha_random == 'Pedra':
    print('Você me ganhou! Papel ganha de pedra.')
elif num == 2 and escolha_random == 'Tesoura':
    print('Você perdeu! Tesoura ganha de papel.')
elif num == 3 and escolha_random == 'Tesoura':
    print('Empate! Tesoura não ganha de tesoura.')
elif num == 3 and escolha_random == 'Papel':
    print('Você me ganhou! Tesoura ganha de papel.')
elif num == 3 and escolha_random == 'Pedra':
    print('Você perdeu! Pedra ganha de tesoura.')


