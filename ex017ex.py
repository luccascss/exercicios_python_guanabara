from math import sqrt, pow
catopo = float(input('Digite o número do cateto oposto: '))
catadj = float(input('Digite o número do cateto adjacente: '))
print('Considerando o cateto oposto {} e o cateto adjacente {}, o valor da Hipotenusa é de {:.2f}'.format(catopo, catadj, sqrt(pow(catopo, 2) + pow(catadj, 2))))
