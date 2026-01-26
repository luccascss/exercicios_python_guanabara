#conversao de um número inteiro para binário, octal ou hexadecimal
num = int(input('Digite um número inteiro: '))
num_choice = int(input('Digite "1" para BINÁRIO, "2" para OCTAL ou "3" para HEXADECIMAL: '))
bin = bin(num).removeprefix("0b")
oct = oct(num).removeprefix("0o")
hex = hex(num).removeprefix("0x")
if num_choice == 1:
    print('O número {} convertido para binário é {}'.format(num, bin))
elif num_choice == 2:
    print('O número {} convertido em octal é {}'.format(num, oct))
elif num_choice == 3:
    print('O número {} convertido para hexadecimal é {}'.format(num, hex))
else:
    print('Tente novamente com alguma opção válida')
