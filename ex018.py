from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo qualquer: '))
radius = radians(ang)
print('O ângulo {}° possui: \nSeno de {:.2f}° \nCosseno de {:.2f}° \nTangente de {:.2f}°'.format(ang, sin(radius), cos(radius), tan(radius)))


