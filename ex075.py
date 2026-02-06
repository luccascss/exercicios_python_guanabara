#programa deve ler 4 inputs e armazena-los em uma tupla, informando dados específicos posteriormente
print('Escolha 04 números interios e digite a seguir:')
tupla_num = tuple(int(input(f'Digite o {i}° número: ')) for i in range(1,5))
# quantidade de aparições do n° 9:
print(f'O n° 9 aparece {tupla_num.count(9)} vezes.')
#posição que aparece o n° 3 primeiro:
if 3 not in tupla_num:
    print('O número 3 não aparece em nenhuma posição.')
else:
    print(f'O n° 3 aparece primeiro na {tupla_num.index(3) + 1}ª posição.')
#Quais são n° pares:
print('Os números pares são: ', end='')
for p in tupla_num:
    if p % 2 == 0:
        print(f'{p}, ', end='')

