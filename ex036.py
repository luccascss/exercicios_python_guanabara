# o programa a seguir avaliará um possível empréstimo bancário, considerando valor do imóvel, salário do comprador e o tempo de financiamento
valor_emprest = float(input('Qual o valor do empréstimo? R$'))
renda = float(input('Qual a sua renda mensal? R$'))
tempo_ano = int(input('Tempo de financiamento em anos: '))
tempo_mes = (tempo_ano * 12)
valor_parcela = (valor_emprest / tempo_mes)
renda_30_porcento = (renda * 30 / 100)
if valor_emprest <= 0 or renda <= 0 or tempo_ano <= 0 or valor_parcela <=0:
    print('Insira valores válidos.')
elif valor_parcela > renda_30_porcento:
    print('Empréstimo negado! A sua renda de R${:.2f} excede o limite de 30% do salário R$({:.2f}) em cima do valor da parcela no valor de R${:.2f}.'.format(renda, renda_30_porcento, valor_parcela))
else:
    print('PARABÉNS! O seu empréstimo no valor de R${:.2f} foi \033[4;33mAPROVADO\033[m com {} parcelas e no valor de R${:.2f} mensal.'.format(valor_emprest, tempo_mes, valor_parcela))
