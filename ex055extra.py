# maior e menor peso dentre cindo pessoas
maior_peso = 0
menor_peso = 0
print('Digite a seguir o peso em Kg de CINCO pessoas e descubra qual o maior e menor entre eles.')
for p in range(1, 6):
    peso = float(input('{}ª pessoa: '.format(p)))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
print('O maior peso foi de {}Kg e o menor foi de {}Kg'.format(maior_peso, menor_peso))

