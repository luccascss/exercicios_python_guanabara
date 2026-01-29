#criação de menu onde leia 2 valores e realize: soma, multiplicação, maior valor, novos números, sair
from time import sleep
valor_escolha = 0
print('Escolha DOIS valores para abrir o menu.')
valor_um = float(input('Digite um valor: '))
valor_dois = float(input('Digite outro valor: '))
while valor_escolha != 5:
    print(f'Valores selecionados: >>>>>> {valor_um} e {valor_dois} <<<<<<')
    print('-' * 50)
    print('Escolha [ 1 ] para soma')
    print('Escolha [ 2 ] para multiplicação')
    print('Escolha [ 3 ] para saber qual o maior valor')
    print('Escolha [ 4 ] para selecionar novos números')
    print('Escolha [ 5 ] para sair do menu')
    valor_escolha = int(input('Digite um valor: '))
    if valor_escolha > 5 or valor_escolha <= 0:
        print('-' * 50)
        print('Você digitou uma opção inválida.')
        print('-' * 50)
    if valor_escolha == 1:
        resultado = 0
        resultado = resultado + (valor_um + valor_dois)
        print('-' * 50)
        print(f'O resultado é: {valor_um} + {valor_dois} = {resultado}')
        print('-' * 50)
    if valor_escolha == 2:
        resultado = 0
        resultado = resultado + (valor_um * valor_dois)
        print('-' * 50)
        print(f'O resultado é: {valor_um} x {valor_dois} = {resultado}')
        print('-' * 50)
    if valor_escolha == 3:
        if valor_um > valor_dois:
            resultado = valor_um
            print('-' * 50)
            print(f'O maior valor entre {valor_um} e {valor_dois} é: {resultado}')
            print('-' * 50)
        elif valor_dois > valor_um:
            resultado = valor_dois
            print('-' * 50)
            print(f'O maior valor entre {valor_um} e {valor_dois} é: {resultado}')
            print('-' * 50)
        else:
            print('-' * 50)
            print(f'Os valores {valor_um} e {valor_dois} são IGUAIS')
            print('-' * 50)
    if valor_escolha == 4:
        print('-' * 50)
        print('Você retornou ao início do menu.')
        print('-' * 50)
        print('Escolha DOIS valores para abrir o menu.')
        valor_um = float(input('Digite um valor: '))
        valor_dois = float(input('Digite outro valor: '))
    if valor_escolha == 5:
        print('Encerrando...')
        sleep(2)
print('=' * 30)
print(f'O programa foi encerrado.')
print('=' * 30)




