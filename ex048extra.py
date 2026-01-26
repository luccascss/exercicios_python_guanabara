#soma de números ímpares que são múltiplos de três entre 1 e 500
soma = 0
contagem = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        contagem = contagem + 1
print('A soma dos {} valores mencionados é de {}'.format(contagem, soma))