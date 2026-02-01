# leitura de números inteiros usando o 999 como condição de parada utilizando break
acumulador = 0
soma = 0
num = int(input('Digite um número inteiro: [Digite 999 para parar] '))
while True:
    if num == 999:
        break
    acumulador = acumulador + 1
    soma = soma + num
    num = int(input('Digite outro número inteiro: [Digite 999 para parar] '))
print(f'Você digitou {acumulador} número(s) e a soma soma foi de {soma}.')
