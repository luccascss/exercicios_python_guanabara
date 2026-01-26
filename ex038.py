#comparação de números inteiros
num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input('Digite outro número inteiro: '))
if num_1 > num_2:
    print('O primeiro número escolhido "{}" é maior que o segundo "{}"'.format(num_1, num_2))
elif num_2 > num_1:
    print('O segundo número escolhido "{}" é maior que o primeiro "{}"'.format(num_2, num_1))
elif num_1 == num_2:
    print('Os números escolhidos "{}" e "{}" são iguais'.format(num_1, num_2))
