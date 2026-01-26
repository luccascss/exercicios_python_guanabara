#leia seis números inteiros e mostre somente a soma
soma_par = 0
soma_impar = 0
lista_par = []
lista_impar = []
for c in range(1, 6 + 1):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0 and num != 0:
        soma_par += num
        lista_par.append(num)
    if num % 2 != 0 and num != 0:
        soma_impar += num
        lista_impar.append(num)
print('Os números pares são {} e a soma deles é {}'.format(lista_par, soma_par))
print('Os números ímpares são {} e a soma deles é {}'.format(lista_impar, soma_impar))





