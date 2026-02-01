#sequência de Fibonacci
print('Descubra a sequência de Fibonacci: ')
num = int(input('Quantos elementos da sequência deseja ver? '))
t_pu = 0 #penúltimo termo
t_u = 1 #último termo
t_n = 0 #n-ésimo termo (termo definido pelo input)
contador = 3 #começa no 3 pois os 2 primeiros termos da sequência são fixos (0 e 1)
if num > 0:
    if num == 1:
        print('0 ➡ FIM')
    elif num == 2:
        print('0 ➡ 1 ➡ FIM')
    elif num >= 3:
        print(f'0 ➡ 1 ➡ ', end='') #primeiros termos da sequência
        while contador <= num:
            contador = contador + 1
            t_n = t_pu + t_u
            if contador <= num:
                print(f'{t_n} ➡ ', end='')
            else:
                print(f'{t_n} ➡ ', end='')
                print('FIM')
            t_pu = t_u
            t_u = t_n
elif num == 0:
    print('Finalizando sem nenhum termo...')
elif num < 0:
    print('Tente novamente com um valor válido.')
print('-' * 50)
print('O programa foi finalizado!')

