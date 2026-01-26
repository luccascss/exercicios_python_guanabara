# o programa a seguir calcula um aumento no salário considerando quanto o indivíduo recebe. Sendo 10% para valores acima de R$1250.00 e 15% para valores menores ou iguais a R$1250.00
valor = float(input('Qual o seu salário? '))
if valor < 0:
    print('Digite um valor válido.')
elif valor > 1250.00:
    print('Considerando o salário de \033[4;32mR${:.2f}\033[m, seu aumento referente a 10% foi de \033[4;32mR${:.2f}\033[m'.format(valor, (valor * 10 / 100)))
else:
    print('Considerando um valor de \033[4;32mR${:.2f}\033[m, seu aumento referente a 15% foi de \033[4;32mR${:.2f}\033[m'.format( valor, (valor * 15 / 100)))

