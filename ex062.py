print('O programa a seguir analisará o primeiro termo e a razão e mostrará sua PA em 10 termos:')
primeiro_termo = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razão: '))
contador = 10
termo = primeiro_termo - razao
add_termo = 1
print(f'A PA escolhida é: ',end='')
while add_termo != 0:
    if add_termo > 0:
        contador = contador + add_termo
        while contador > 0:
            contador = contador - 1
            termo = termo + razao
            if contador > 0:
                print(f'{termo} ➡ ', end= '')
            else:
                print(f'{termo} ➡ FIM')
    add_termo = int(input('Quer adicionar mais quantos termos? '))
    if add_termo == 0:
        print('Finalizando...')
    elif add_termo < 0:
        print('Digite uma opção válida.')
print('=' * 40)
