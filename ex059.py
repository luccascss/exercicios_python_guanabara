#criação de menu onde leia 2 valores e realize: soma, multiplicação, maior valor, novos números, sair
resultado = 0
print('Escolha DOIS valores para abrir o menu.')
valor_um = float(input('Digite um valor: '))
valor_dois = float(input('Digite outro valor: '))
print('''Escolha [ 1 ] para SOMA
Escolha [ 2 ] para MULTIPLICAÇÃO
Escolha [ 3 ] para saber qual o maior valor
Escolha [ 4 ] para selecionar novos números
Escolha [ 5 ] para sair do menu''')
valor_escolha = int(input('Digite sua escolha: '))
while valor_escolha != 5:
    if valor_escolha > 5 or valor_escolha <= 0:
        print('''Escolha [ 1 ] para SOMA
Escolha [ 2 ] para MULTIPLICAÇÃO
Escolha [ 3 ] para saber qual o maior valor
Escolha [ 4 ] para selecionar novos números
Escolha [ 5 ] para encerrar o programa''')
        valor_escolha = int(input('Digite uma opção válida: '))
    if valor_escolha == 1:
        resultado = resultado + (valor_um + valor_dois)
        print('-' * 40)
        print(f'O resultado {valor_um} + {valor_dois} = {resultado}')
        print('-' * 40)
        print('''Escolha [ 1 ] para SOMA
Escolha [ 2 ] para multiplicação
Escolha [ 3 ] para saber qual o maior valor
Escolha [ 4 ] para selecionar os novos números
Escolha [ 5 ] para para o programa''')
        valor_escolha = int(input('Digite sua escolha: '))
    if valor_escolha == 2:
        resultado = resultado + (valor_um * valor_dois)
        print('-' * 40)
        print(f'O resultado é: {valor_um} x {valor_dois} = {resultado}')
        print('-' * 40)
        print('''Escolha [ 1 ] para SOMA
Escolha [ 2 ] para multiplicação
Escolha [ 3 ] para saber qual o maior valor
Escolha [ 4 ] para selecionar os novos números
Escolha [ 5 ] para sair do menu''')
        valor_escolha = int(input('Digite sua escolha: '))
    if valor_escolha == 3:
        if valor_um > valor_dois:
            resultado = valor_um
            print('-' * 40)
            print(f'O maior valor entre {valor_um} e {valor_dois} é: {resultado}')
            print('-' * 40)
            print('''Escolha [ 1 ] para SOMA
Escolha [ 2 ] para multiplicação
Escolha [ 3 ] para saber qual o maior valor
Escolha [ 4 ] para selecionar os novos números
Escolha [ 5 ] para sair do menu''')
            valor_escolha = int(input('Digite sua escolha: '))
        elif valor_dois > valor_um:
            resultado = valor_dois
            print('-' * 40)
            print(f'O maior valor entre {valor_um} e {valor_dois} é: {resultado}')
            print('-' * 40)
            print('''Escolha [ 1 ] para SOMA
Escolha [ 2 ] para multiplicação
Escolha [ 3 ] para saber qual o maior valor
Escolha [ 4 ] para selecionar os novos números
Escolha [ 5 ] para sair do menu''')
            valor_escolha = int(input('Digite sua escolha: '))
        else:
            print('-' * 40)
            print(f'Os valores {valor_um} e {valor_dois} são IGUAIS')
            print('-' * 40)
            print('''Escolha [ 1 ] para SOMA
Escolha [ 2 ] para multiplicação
Escolha [ 3 ] para saber qual o maior valor
Escolha [ 4 ] para selecionar os novos números
Escolha [ 5 ] para sair do menu''')
            valor_escolha = int(input('Digite sua escolha: '))
    if valor_escolha == 4:
        print('Você retornou ao início do menu.')
        valor_um = float(input('Digite um valor: '))
        valor_dois = float(input('Digite outro valor: '))
        print('''Escolha [ 1 ] para SOMA
Escolha [ 2 ] para multiplicação
Escolha [ 3 ] para saber qual o maior valor
Escolha [ 4 ] para selecionar os novos números
Escolha [ 5 ] para sair do menu''')
        valor_escolha = int(input('Digite sua escolha: '))
print('-' * 40)
print(f'O programa foi encerrado.')
print('-' * 40)




