#palíndromo
frase = str(input('Digite uma frase: ')).strip().replace(' ', '').upper()
if frase == frase[::-1]:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')





