# leia vários números inteiros e só pare quando digitar o número 999 (flag). Após, mostra quantos números foram digitados e a soma entre eles.
soma = 0
acumulador = 0
print('Para parar o programa, digite "999"')
num = int(input('Digite um número inteiro: '))
while num != 999:
    soma = soma + num
    acumulador = acumulador + 1
    num = int(input('Digite outro número inteiro: '))
print(f'Você digitou {acumulador} números e a soma desses números é de {soma}')
