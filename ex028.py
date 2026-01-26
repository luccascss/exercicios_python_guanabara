from random import randint
print('No programa a seguir, o computador "pensará" em um número inteiro entre 0 a 5 e você deverá tentar adivinhar esse número: ')
numr = randint(0, 5)
num = int(input('Digite um número conforme as regras: '))
if numr == num:
    print('Parabéns, você acertou! O número foi: {}'.format(numr))
elif num > 5 or num < 0:
    print('Você digitou um número inválido, tente novamente!')
else:
    print('Não foi dessa vez! O número escolhido foi: {}'.format(numr))
print('----FIM----')

