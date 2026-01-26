# gerenciador de pagamentos
valor = float(input('Qual o valor do produto? R$')).__abs__()
print('''[ 1 ] Pagamento à vista (10% de desconto)
[ 2 ] Pagamento à vista no cartão (5% de desconto)
[ 3 ] Pagamento 2x no cartão (sem juros)
[ 4 ] Pagamento 3x ou mais no cartão (20% de juros)''')
escolha = int(input('Selecione uma opção: '))
if escolha == 1:
    diferenca = ((valor * 10) / 100)
    valor_final = (valor - diferenca)
elif escolha == 2:
    diferenca = ((valor * 5) / 100)
    valor_final = (valor - diferenca)
elif escolha == 3:
    valor_final = valor
    print('O parcelamento ficou em 2x de R${:.2f}'.format(valor_final / 2))
elif escolha == 4:
    diferenca = ((valor * 20) / 100)
    valor_final = (valor + diferenca)
    parcela = int(input('Em quantas vezes deseja parcelar (máx 12x)? ')).__abs__()
    if parcela > 12 or parcela == 0:
        print('Escolha inválida. Tente novamente!')
    else:
        print('O parcelamento ficou em {}x de R${:.2f}'.format(parcela, (valor_final / parcela)))
else:
    valor_final = '????'
    print('Escolha uma opção válida.')
print('O produto no valor de R${}, tem seu valor final de R${}'.format(valor, valor_final))
