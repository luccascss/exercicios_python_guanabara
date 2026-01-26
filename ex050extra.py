#soma de números pares inteiros, se for ímpar desconsidere-o
soma = 0 #acumulador
contagem = 0 #contador
print('Digite SEIS números inteiros e descubra a soma daqueles que forem par!')
for c in range(1, 7):
    num = int(input('{}° número: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        contagem = contagem + 1
print('Considerando o(s) {} número(s) par(es) digitado(s), sua soma é {}.'.format(contagem, soma))

