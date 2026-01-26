#computador "pensará" em um número inteiro entre 0 a 10 e você deverá tentar adivinhar esse número
from random import randint
from time import sleep
jogador_soma = 1
computador = randint(0, 10)
print('Nesse jogo, eu pensarei em um número entre 0 e 10 e cabe a você descobrir que número é esse!')
jogador = int(input('Digite seu palpite: '))
while computador != jogador: #loop até que o jogador acerte o número escolhido pelo computador
    if jogador > 10 or jogador < 0:
        print('Sem bancar o espertinho hein....')
        sleep(2)
        jogador = int(input('Digite seu palpite novamente: '))
    else:
        if computador != jogador:
            jogador_soma = jogador_soma + 1
            print('Foi quase... Continue tentando que uma hora vai!!!')
            jogador = int(input('Digite seu palpite novamente: '))
#computador == jogador (está fora do while pois o mesmo acaba assim que a condição é alcançada)
if jogador_soma == 1:
    print('Você acertou de primeira... INACREDITÁVEL!!!!!')
    sleep(2)
    print('Sério, não acredito em você. Você espiou o meu código né?!!')
    sleep(3)
    print('......')
    sleep(1)
    print('Enfim...')
    sleep(1)
    print('Meus parabéns seu trapaceiro!')
else:
    print('Droga....')
    sleep(2)
    print(f'Você acertou após {jogador_soma} tentativas! O número que eu estava "pensando" era {computador}')
    print('PARABÉNS!!!')
print('=' * 100)