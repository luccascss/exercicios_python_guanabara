# cálculo de média escolar
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = ((nota_1 + nota_2) / 2)
if media > 10.0 or media < 0:
    print('Digite valor válidos.')
elif media < 5.0:
    print('Considerando as notas {} e {}, sua média foi de {:.2f}. REPROVADO!'.format(nota_1, nota_2, media))
elif media >= 7.0:
    print('Considerando as notas {} e {}, sua média foi de {:.2f}. APROVADO!'.format(nota_1, nota_2, media))
else:
    print('Considerando as notas {} e {}, sua média foi de {:.2f}. RECUPERAÇÃO!'.format(nota_1, nota_2, media))
