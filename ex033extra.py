num_1 = float(input('Primeiro valor: '))
num_2 = float(input('Segundo valor: '))
num_3 = float(input('Terceiro valor: '))
#verificando maior valor:
if num_1 > num_2 and num_1 > num_3:
    maior = num_1
elif num_2 > num_1 and num_2 > num_3:
    maior = num_2
elif num_3 > num_1 and num_3 > num_2:
    maior = num_3
# calculando o menor valor:
if num_1 < num_2 and num_1 < num_3:
    menor = num_1
elif num_2 < num_1 and num_2 < num_3:
    menor = num_2
elif num_3 < num_1 and num_3 < num_2:
    menor = num_3
print('O maior valor é {} e o menor é {}'.format(maior, menor))

