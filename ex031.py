distancia = float(input('Qual a distância da viagem em Km? '))
if distancia <= 200.0:
    print('Considerando a distância de {}Km, e um ticket de R$0,50 por Km, o valor da passagem é de: R${:.2f}'.format(distancia, distancia * 0.50))
else:
    print('Considerando a distância de {}Km, e um ticket de R$0,45 por km, o valor da passagem é de: R${:.2f}'.format(distancia, distancia * 0.45))
