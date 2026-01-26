km = float(input('Qual a quantidade de Quilômetros rodados? '))
d = int(input('Por quantos dias o carro foi alugado? '))
pago = (km * 0.15) + (d * 60)
print('Considerando {}Km percorridos e {} dias alugados, o valor a pagar é de R$ {:.2f}'.format(km, d, pago))





