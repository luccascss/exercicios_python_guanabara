# leia palavavras dentro de uma tupla e mostre apenas as suas vogais
tupla_palavras = ('aprender', 'programar', 'linguaguem', 'python', 'curso',
         'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
         'programador', 'futuro')
vogais = 'aeiou'
# separa a tupla em palavras
for palavra in tupla_palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ',end='')
    # separa cada palavra em letras
    for letra in palavra:
        # verifica se letra é uma vogal
        if letra in vogais:
            print(f'{letra} ', end='')
