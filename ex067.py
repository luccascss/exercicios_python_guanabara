#tabuada de diversos inputs até que o usuário escolha um número negativo
print('Digite um número para ver sua tabuada!')
while True:
    contador = 0
    print('=' * 38)
    num = int(input('Digite um número: '))
    print('=' * 38)
    if num < 0:
        print('Finalizando...')
        print('=' * 38)
        break
    else:
        while contador < 10:
            contador = contador + 1
            print(f'{num} x {contador} = {num * contador}')
print('Programa encerrado.')