#contagem por extenso usando tupla
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número de 0 até 20: '))
while num < 0 or num > 20:
    num = int(input('Número inválido! Digite um número de 0 até 20: '))
print(f'O número escolhido foi {num}: {numeros[num].upper()}')