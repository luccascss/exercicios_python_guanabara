# o programa a seguir calcula um aumento no salário considerando quanto o indivíduo recebe. Sendo 10% para valores acima de R$1250.00 e 15% para valores menores ou iguais a R$1250.00
valor = float(input('Digite o valor do salário: R$'))
valor_10_porcento = (valor * 10 / 100)
valor_15_porcento = (valor * 15 / 100)
if valor < 0:
    input('Digite um valor válido.')
elif valor > 1250.00:
    input('Considerando o valor de R${}, seu aumento foi de 10% (R${:.2f}), totalizando o salário de R${:.2f}'.format(valor, valor_10_porcento, (valor + valor_10_porcento)))
else:
    input('Considerando o valor de R${} seu aumento foi de 15% (R${:.2f}), totalizando o salário de R${:.2f}'.format(valor, valor_15_porcento, (valor + valor_15_porcento)))

