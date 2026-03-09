# faça uma função com nome contador() que receba 3 parâmetros: início, fim e passo e realize a contagem
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim:
        fim = fim - 1
    if fim > inicio:
        fim = fim + 1
    if inicio > fim and passo > 0 or fim > inicio and passo < 0:
        passo = passo * -1
    for cont in range(inicio, fim, passo):
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
