# Crie uma lista chamada "números" e duas funções chamadas "sorteia()" e "somapar()". Onde a primeira vai sortear 5 números aleatórios e a segunda vai somar os números pares sorteados
from random import randint
def sorteia():
    num = list()
    for _ in range(5):
        num.append(randint(1, 10))
    print(f'Os números sorteados foram {num}')
    return num
def somapar(lst):
    soma = 0
    for valor in lst:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares é de {soma}')


#programa principal
somapar(sorteia())

