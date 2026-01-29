if valor_escolha == 1:
    print(f'A soma dos valores {valor_um} e {valor_dois} é igual a {(valor_um + valor_dois)}')
elif valor_escolha == 2:
    print(f'A multiplicação dos valores {valor_um} e {valor_dois} é igual a {(valor_um * valor_dois)}')
elif valor_escolha == 3:
    if valor_um > valor_dois:
        print(f'O maior valor entre {valor_um} e {valor_dois} é {valor_um}')
    elif valor_dois > valor_um:
        print(f'O maior valor entre {valor_um} e {valor_dois} é {valor_dois}')
    else:
        print(f'Os valores {valor_um} e {valor_dois} são iguais')
if valor_escolha == 4:
    valor_um = float(input('Digite um número: '))
    valor_dois = float(input('Digite outro número: '))