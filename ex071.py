#simulador de caixa eletrônico
num = float(input('Qual o valor a ser sacado? R$ '))
valor = int(num)
cedula_50 = 0
cedula_20 = 0
cedula_10 = 0
cedula_1 = 0
while valor != 0:
    while valor >= 50:
        valor = valor - 50
        cedula_50 = cedula_50 + 1
        if valor < 0:
            valor = valor + 50
            break

    while valor >= 20:
        valor = valor - 20
        cedula_20 = cedula_20 + 1
        if valor < 0:
            valor = valor + 20
            break

    while valor >= 10:
        valor = valor - 10
        cedula_10 = cedula_10 + 1
        if valor < 0:
            valor = valor + 10
            break

    while valor > 0:
        valor = valor - 1
        cedula_1 = cedula_1 + 1

print(f'Total de {cedula_50} cédulas de R$50')
print(f'Total de {cedula_20} cédulas de R$20')
print(f'Total de {cedula_10} cédulas de R$10')
print(f'Total de {cedula_1} cédulas de RS1')