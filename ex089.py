# Guarde lista dentro de listas dentro de lista
dados = list() # [nome[0], notas[1], média[2]], [nome[0], notas[1], média[2]], ...
resp = ''
print('========== COLÉGIO GALOTITO ===========')
while True:
    nome = str(input('Nome: ')).strip().upper()
    nota_01 = float(input('1ª nota: '))
    nota_02 = float(input('2ª nota: '))
    media = ((nota_01 + nota_02) / 2)
    dados.append([nome, [nota_01, nota_02], media])
    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resp != 'S' and resp != 'N':
            print('Escolha [ S ] para sim')
            print('Escolha [ N ] para não')
    if resp == 'S':
        resp = ''
    elif resp == 'N':
        break
print('=' * 30)
print('REFERÊNCIA (N°: NOME -> MÉDIA)')
print('-' * 30)
for i, d in enumerate(dados):
    print(f'{i + 1}: {d[0]} -> {d[2]}')
print('-' * 80)
print('Escolha um número referente a um aluno para ver suas notas separadamente:')
num = -1 # variável de controle do loop
while num != 998:
    print('[ 999 ] para finalizar')
    num = int(input('Digite sua escolha: ')) - 1
    print('-' * 30)
    if num == 998:
        print('Finalizando...')
    elif num >= len(dados):
        print('Digite um valor válido!')
        print('-' * 30)
    else:
        print(f'Notas do(a) {dados[num][0]}: {dados[num][1]}')
        print('-' * 30)
print('=' * 30)
