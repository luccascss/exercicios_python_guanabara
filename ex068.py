#jogo par ou ímpar, o programa só será encerrado caso o jogador perca
from random import randint
print('Escolha um número de 0 a 10 e tente me ganhar no par ou ímpar!')
while True:
    jogador = int(input('Digite um número: '))
    soma = 0
    escolha = 0
    computador = randint(0, 10)
    if jogador < 0 and jogador > 10:
        print('Escolha um número válido...')
        print('Quantos dedos tem na sua mão mesmo???')
        num = int(input('Digite um número: '))
        soma = soma + (computador + jogador)
    else:
        while True:
            if escolha == 1:
                print('Você escolheu PAR! Eu fico com ímpar então...')
                break
            elif escolha == 2:
                print('Você escolheu ÍMPAR! Eu fico com PAR então...')
                break
            else:
                print('Escolha uma opção válida...')
                escolha = int(input('Par [1] ou ímpar [2]? '))
    if soma % 2 == 0:
        if escolha == 1:
            print(f'A soma deu {soma}... Você GANHOU!!!')
        else:
            print(f'A soma deu {soma}... Você PERDEU!!!')
    elif soma % 2 != 0:
        if escolha == 1:
            print(f'A soma deu {soma}... Você PERDEU!!!')
        else:
            print(f'A soma deu {soma}... Você GANHOU!!!')


