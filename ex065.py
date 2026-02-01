#calcular média, maior e menor valor considerando inputs até que o usuário deseje parar
condicao_parada = ''
soma_num = 0
contador = 0
num = 0
maior_num = 0
menor_num = 0
while condicao_parada != 'S':
    num = int(input('Digite um número inteiro: '))
    soma_num = soma_num + num
    contador = contador + 1
    if contador == 1:
        maior_num = num
        menor_num = num
    else:
        if num > maior_num:
                maior_num = num
        elif num < menor_num:
                menor_num = num
    condicao_parada = str(input('Deseja parar? [S/N]: ')).strip().upper()
media = (soma_num / contador)
print(f'A média dos números foi de {media:.2f}')
print(f'O maior número digitado foi {maior_num} e o menor foi {menor_num}.')
