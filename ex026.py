from itertools import count

texto = str(input('Digite uma frase qualquer:' )).strip().lower()
print('Quantas vezes aparecem a letra "A"? {}'.format(texto.count("a")))
print('Em que posição a letra "A" aprece a primeira vez? {} '.format(texto.find("a")+1))
print('Em que posição a letra "A" aparece pela última vez? {}'.format(texto.rfind("a")+1))


