#simulador de caixa eletrônico
print('=' * 30)
print(f'{'BANCO GALOTITO':^30}')
print('=' * 30)
num = float(input('Qual o valor a ser sacado? R$'))
valor = int(num)
cedula_50 = 0 #nº de cédulas de R$ 50 usadas
cedula_20 = 0 #nº de cédulas de R$20 usadas
cedula_10 = 0 #nº de cédulas de R$10 usadas
cedula_1 = 0 #nº de cédulas de R$1 usadas
while True:
    # loop para cédulas de 50
    while valor >= 50:
        valor = valor - 50
        cedula_50 = cedula_50 + 1
    if cedula_50 > 0:
        print(f'Total de {cedula_50} cédulas de R$50')
    #loop para cédulas de 20
    while valor >= 20:
        valor = valor - 20
        cedula_20 = cedula_20 + 1
    if cedula_20 > 0:
        print(f'Total de {cedula_20} cédulas de R$20')
    #loop para cédulas de 10
    while valor >= 10:
        valor = valor - 10
        cedula_10 = cedula_10 + 1
    if cedula_10 > 0:
        print(f'Total de {cedula_10} cédulas de R$10')
    #loop para cédulas de 1
    while valor >= 1:
        valor = valor - 1
        cedula_1 = cedula_1 + 1
    if cedula_1 > 0:
        print(f'Total de {cedula_1} cédulas de RS1')
    break
print('=' * 30)
print('Volte sempre e caso tenha, não me peça os centavos...')