#programa que leia o NOME e PREÇO de vários produtos até que o usuário deseja parar
total_preco = 0 #soma dos valores de todos os produtos
acumulador_valor = 0 #acumulador para valores de 1000 reais ou mais
menor_preco_nome = ''
menor_preco = 0
contador_preco = 0
print('----- ATACADÃO GALOTITO -----')
print('=' * 30)
while True:
    nome_produto = str(input('Nome do produto: ')).strip().upper()
    while True:
        preco_produto = float(input('Preço: R$'))
        if preco_produto < 0:
            print('-' * 25)
            print('Digite um valor válido: ')
            print('-' * 25)
        else:
            contador_preco = contador_preco + 1
            total_preco = total_preco + preco_produto
            break
    # contador para definir que o primeiro produto digitado possui o menor valor
    if contador_preco == 1:
        menor_preco = preco_produto
        menor_preco_nome = nome_produto
    # regra para definir o produto de menor valor
    if preco_produto < menor_preco:
        menor_preco = preco_produto
        menor_preco_nome = nome_produto
    # regra para calcular a soma de todos os valores válidos inputados
    if preco_produto >= 1000:
        acumulador_valor = acumulador_valor + 1
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if continuar != 'S' and continuar != 'N':
            print('-' * 30)
            print('Escolha [ S ] para SIM')
            print('Escolha [ N ] para NÃO')
            print('-' * 30)
        else:
            break
    if continuar == 'N':
        print('=' * 20)
        print('Finalizando...')
        print('=' * 20)
        break
print(f'O total gasto na compra foi de R${total_preco:.2f}')
print(f'Ao todo, {acumulador_valor} produtos custam R$1000.00 ou mais.')
print(f'O produto mais barato foi {menor_preco_nome} com o valor de R${menor_preco:.2f}.')
