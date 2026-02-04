#contagem por extenso usando tupla
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
#evitar deixar linhas de código muito longas!!!
while True:
    continuar = ''
    num = -1
    while num < 0 or num > 20:
        num = int(input('Digite um número de 0 até 20: '))
        if num < 0 or num > 20:
            print('Número inválido. Tente novamente! ')
        else:
            print(f'O número escolhido foi {num}: {numeros[num].upper()}')
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if continuar != 'S' and continuar != 'N':
            print('Escolha [ S ] para SIM')
            print('Escolha [ N ] para NÃO')
    if continuar == 'N':
        print('Finalizando...')
        break
print('Programa finalizado.')
