# cálculo de IMC
peso = str(input('Digite o seu peso: (KG) ')).replace(",", ".")
altura = str(input('Digite a sua altura: (M) ')).replace(".", "").replace(",", "")
altura_float = float(altura)
peso_float = float(peso)
imc = peso_float / ((altura_float / 100) ** 2)
if imc < 18.5:
    print('Considerando o peso de {}kg e altura de {}cm, seu IMC é de {:.2f}: ABAIXO DO PESO'.format(peso, altura, imc))
elif 18.5 <= imc < 25.0:
    print('Considerando o peso de {}kg e altura de {}cm, seu IMC é de {:.2f}: PESO IDEAL'.format(peso, altura, imc))
elif 25.0 <= imc < 30.0:
    print('Considerando o peso de {}kg e altura de {}cm, seu IMC é de {:.2f}: SOBREPESO'.format(peso, altura, imc))
elif 30.0 <= imc < 40.0:
    print('Considerando o peso de {}kg e altura de {}cm, seu IMC é de {:.2f}: OBESIDADE'.format(peso, altura, imc))
elif imc >= 40.0:
    print('Considerando o peso de {}kg e altura de {}cm, seu IMC é de {:.2f}: OBESIDADE MÓRBIDA'.format(peso, altura, imc))
