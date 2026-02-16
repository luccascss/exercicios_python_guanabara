# Leia 7 valores numéricos e os coloque numa única lista que mantenha os valores pares e ímpares separadas. No fim, mostre os valores em ordem crescente.
num_lista = list() # par / ímpar respectivamente
par =  list()
impar = list()
cont = 0
for _ in range (7):
    cont = cont + 1
    num = int(input(f'Digite o {cont}° valor: '))
    if num % 2 == 0: #par
        par.append(num)
    if num % 2 != 0: #ímpar
        impar.append(num)
par.sort()
impar.sort()
num_lista.insert(0, par[:])
num_lista.insert(1, impar[:])
print(f'Valores pares: {num_lista[0]}')
print(f'Valores ímpares: {num_lista[1]}')
