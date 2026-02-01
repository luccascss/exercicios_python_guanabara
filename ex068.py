#jogo par ou ímpar, o programa só será encerrado caso o jogador perca
from random import randint
vitoria = 0
while True:
    soma = 0
    escolha = 0
    jogador = -1
    computador = randint(0, 10)
    while jogador > 10 or jogador < 0:
        print('Escolha um número de 0 a 10 e tente me ganhar no par ou ímpar!')
        jogador = int(input('Escolha seu número: '))
        print('=' * 40)
        if jogador > 10 or jogador < 0:
            print('Escolha um número válido... ')
            print('=' * 40)
        else:
            soma = soma + (jogador + computador)
    while escolha != 1 and escolha != 2:
        print('Escolha PAR [1] ou ÍMPAR [2]:')
        escolha = int(input('Digite sua escolha: '))
        print('=' * 40)
        if escolha != 1 and escolha != 2:
            print('Escolha um valor válido...')
            print('=' * 40)
        else:
            if escolha == 1:
                print('Você escolheu PAR!')
                print('=' * 40)
            elif escolha == 2:
                print('Você escolheu ÍMPAR!')
                print('=' * 40)
    if soma % 2 == 0: #par
        if escolha == 1:
            print(f'Você jogou {jogador} e o computador {computador}. A soma deu {soma}')
            print('Jogador VENCEU!')
            print('=' * 40)
        else:
            print(f'Você jogou {jogador} e o computador {computador}. A soma deu {soma}')
            print('Computador VENCEU!')
            print('=' * 40)
    elif soma % 2 != 0: #ímpar
        if escolha == 1:
            print(f'Você jogou {jogador} e o computador {computador}. A soma deu {soma}')
            print('Computador VENCEU!')
            print('=' * 40)
        else:
            print(f'Você jogou {jogador} e o computador {computador}. A soma deu {soma}')
            print('Jogador VENCEU!')
            print('=' * 40)
    if soma % 2 == 0 and escolha == 1 or soma % 2 != 0 and escolha == 2:
        vitoria = vitoria + 1
    elif soma % 2 == 0 and escolha == 2 or soma % 2 != 0 and escolha == 1:
        break
print(f'O jogo acabou! Você ganhou {vitoria} vezes.')
print('=' * 40)
print('Programa Finalizado!')

