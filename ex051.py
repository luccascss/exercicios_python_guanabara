# primeiro termo e razão PA
num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
for termo in range(1, 10 + 1):
    print(num + (termo - 1) * razao)
