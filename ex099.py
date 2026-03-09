# Crie uma função maior() que receba vários parâmetros que possa dizer qual dos valores é o maior
def maior(lst):
    m = lst[0]
    for n in lst:
        if n > m:
            m = n
    print(f'Dos valores digitados {lst}, o maior é {m}.')


lista_num = list()
while True:
    num = int(input('Escolha um valor inteiro [999 para encerrar]: '))
    if num == 999:
        break
    lista_num.append(num)
if len(lista_num) == 0:
    lista_num.append(0)
maior(lista_num)
