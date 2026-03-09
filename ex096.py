 # calcule a área utilizando função
def area(comprimento, largura):
    a = comprimento * largura
    print(f'A área do terreno {comprimento}x{largura} é de {a:.1f}m².')


#programa principal
c = float(input('Comprimento (m): '))
l = float(input('Largura (m): '))
area(c, l)

