# valor a ser pago pelo produto considerando a forma de pagamento
valor = float(input('Qual o valor de produto: R$ ')).__abs__()
modo_pag = int(input('Escolha "1" para pagamento à vista dinheiro/cheque com 10% de desconto; \n'
                     'Escolha "2" para pagamento à vista no cartão com 5% de desconto; \n'
                     'Escolha "3" para pagamento em 2x no cartão; \n'
                     'Escolha "4" para pagamento em 3x ou mais no cartão com 20% de juros; \n'
                     'Digite sua forma de pagamento: ')).__abs__()
if modo_pag > 4 or modo_pag == 0:
    print('Escolha uma opção válida')
elif modo_pag == 1:
    print('O produto no valor de R${} com 10% de desconto (R${:.2f}), tem seu valor final de R${:.2f}'.format(valor, (valor * 10 / 100), valor - (valor * 10 / 100)))
elif modo_pag == 2:
    print('O produto no valor de R${} com 5% de desconto (R${:.2f}), tem seu valor final de R${:.2f}'.format(valor, (valor * 5 / 100), (valor - (valor * 5 / 100))))
elif modo_pag == 3:
    print('O produto tem seu valor final de R${}, em 2x no cartão'.format(valor))
elif modo_pag == 4:
    print('O produto no valor de R${} com 20% de juros (R${:.2f}), tem seu valor final de R${:.2f}'.format(valor, (valor * 20 / 100), (valor + (valor * 20 / 100))))

