#identificador de palíndromos
frase = str(input('Digite uma frase: ')).strip().upper()
frase_separada = frase.split()
frase_junta = ''.join(frase_separada)
frase_invertida = ''
for letra in frase_junta:
    frase_invertida = letra + frase_invertida
if frase_junta == frase_invertida:
    print('As frases {} e {} são um palíndromo!'.format(frase_junta, frase_invertida))
else:
    print('As frases {} e {} não são um palíndromo!'.format(frase_junta, frase_invertida))
