#tupla ÚNICA com nome e preço de produtos. No final, mostre uma tabela organizando seus valores
produtos = ('Caneta', 2.50, 'Borracha', 1.00, 'Estojo', 10.50, 'Compasso', 9.99, 'Livro', 34.90)
print('=' * 40)
print(f'{"Listagem de preços":^40}')
print('=' * 40)
for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<30}', end='')
    else:
        print(f'R${produtos[posicao]:.2f}')
print('-' * 40)

