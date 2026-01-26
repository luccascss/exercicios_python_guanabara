import math
catetoadj = float(input('Qual o valor do cateto adjacente: '))
catetoopo = float(input('QUal o valor do cateto oposto? '))
'''print('Considerando o cateto adjacente {} e o cateto oposto {}, o valor da hipotenusa é {:.2f}'.format(catetoadj, catetoopo, math.sqrt(math.pow(catetoadj,2) + math.pow(catetoopo,2))))'''
'''print('O valor da hipotenusa é de {:.2f}'.format(math.hypot(catetoadj, catetoopo)))'''
print('O valor da hipotenusa é {:.2f}'.format((catetoadj ** 2 + catetoopo ** 2) ** 0.5))




