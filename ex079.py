#leia vários inputs e coloque os valores em uma lista, sem add valores repetidos e no fim mostrando no terminal os mesmos valores em ordem crescente
cont = ''
lista_num = list()
while True:
    num = int(input('Digite um número: '))
    if num in lista_num:
        print('Valor escolhido já existente na lista...')
    else:
        lista_num.append(num)
        print('Valor adicionado com sucesso...')
    while cont != 'N' and cont != 'S':
        cont = str(input('Deseja continuar? ')).strip().upper()
        if cont != 'N' and cont != 'S':
            print('Digite uma opção válida...')
    if cont == 'N':
        break
    else:
        cont = ''
lista_num.sort()
print('=' * 50)
print(f'Você digitou os valores {lista_num}')
