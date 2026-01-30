print('O programa a seguir analisará o primeiro termo e a razão e mostrará sua PA em 10 termos:')
primeiro_termo = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razão: '))
contador = 1
termo = primeiro_termo
add_termo = 10
total = 0
print(f'A PA escolhida é: ',end='')
while add_termo != 0:
    if add_termo > 0:
        total = total + add_termo
        while contador <= total:
            print(f'{termo} ➡ ', end='')
            contador = contador + 1
            termo = termo + razao
    print('FIM')
    add_termo = int(input('Quer adicionar mais quantos termos? '))
    if add_termo == 0:
        print('Finalizando...')
    elif add_termo < 0:
        print('Digite uma opção válida.')
print('=' * 40)
print(f'PA finalizada com um total de {total} termos')