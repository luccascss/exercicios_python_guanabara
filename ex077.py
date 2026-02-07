# leia palavavras dentro de uma tupla e mostre apenas as suas vogais
tupla = ('aprender', 'programar', 'linguaguem', 'python', 'curso',
         'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
         'programador', 'futuro')
vogais = 'aeiou'
for c in range(0, len(tupla)):
    print(f'Na palavra {tupla[c].upper()} temos: ',end='')
    for letra in tupla[c]:
        if letra in vogais:
            print(f'{letra} ', end='')
    print()