alt = float(input('Altura da parede em metros: '))
larg = float(input('Largura da parede em metros: '))
area = alt * larg
l = area * 1 / 2
print('Considerando uma parede com {}m de altura e {}m de largura, sua Área é de {:.2f}m2'.format(alt, larg, area))
print('Com uma área de {:.2f}m2, é necessário {:.2f}L de tinta'.format(area, l))

