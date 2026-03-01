# faça uma função com nome contador() que receba 3 parâmetros: início, fim e passo e realize a contagem
def contador(a, b, c):
    if c == 0:
        c = 1
    if a > b:
        b = b - 1
    if b > a:
        b = b + 1
    if a > b and c > 0 or b > a and c < 0:
        c = c * -1
    for cont in range(a, b, c):
        print(f'{cont}, ',end='')
    print('FIM!')
def linha():
    print('=' * 40)


# programa principal
linha()
print(f'Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
linha()
print(f'Contagem de 10 até 0 de 2 em 2')
contador(10, 0, -2)
linha()
print('Personalize a contagem conforme desejar: ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
    print(f'Contagem de {inicio} até {fim} de 1 em 1')
elif passo < 0:
    print(f'Contagem de {inicio} até {fim} de {passo * -1} em {passo * -1}')
linha()
contador(inicio, fim, passo)
