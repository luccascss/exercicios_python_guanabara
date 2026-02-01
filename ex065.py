#calcular média, maior e menor valor considerando inputs até que o usuário deseje parar
condicao_parada = ''
soma_num = 0
acumulador_num = 0
num = 0
maior_num = 0
menor_num = 0
while condicao_parada != 'S':
    num = int(input('Digite um número inteiro: '))
    soma_num = soma_num + num
    acumulador_num = acumulador_num + 1
    if acumulador_num == 1:
        maior_num = num
        menor_num = num
    elif num > maior_num:
            maior_num = num
    elif num < menor_num:
            menor_num = num
    condicao_parada = str(input('Deseja parar? [S/N]: ')).strip().upper()
    if condicao_parada != 'S' and condicao_parada != 'N':
        condicao_parada = str(input('Digite uma opção válida [S/N]: '))
print(f'A média dos números foi de {(soma_num / acumulador_num):.2f}')
print(f'O maior número digitado foi {maior_num} e o menor foi {menor_num}.')
