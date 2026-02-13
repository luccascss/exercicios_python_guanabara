# analise uma expressão numérica e diga se ela é válida ou não
contador_abre = 0
contador_fecha = 0
num = str(input('Digite uma expressão númerica: ')).strip()
for letra in num:
    if letra == '(':
        contador_abre = contador_abre + 1
    elif letra == ')':
        contador_fecha = contador_fecha + 1
if contador_abre == contador_fecha:
    print('A expressão é válida!')
else:
    print('A expressão não é válida!')
