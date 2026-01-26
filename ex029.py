print('Cálculo de multas 2026')
velocidade_carro = float(input('Qual a velocidade máxima atingida? '))
multa = (velocidade_carro - 80.0) * 7
if velocidade_carro < 0:
    print('Digite um valor válido.')
elif velocidade_carro <= 80.0:
    print('Seu veículo estava dentro dos limites da rodovia.')
else:
    print('Você estava a {}Km/h, valor acima dos limites de velocidade da rodovia de 80Km/h.'.format(velocidade_carro))
    print('A multa para essa infração é de: R${:.2f}'.format(multa))
print('------FIM------')


