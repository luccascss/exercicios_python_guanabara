#dez primeiros termos de uma PA
print('O programa a seguir analisará o primeiro termo e a razão e mostrará sua PA em 10 termos:')
primeiro_termo = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razão: '))
contador = 0
termo = primeiro_termo - razao
print(f'A PA escolhida é: (',end='')
while contador < 10:
    contador = contador + 1
    termo = termo + razao
    print(f'{termo}', end= '')
    print(')' if contador > 9 else ' ➡ ', end= '')
