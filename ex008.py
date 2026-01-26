m = float(input('Valor em metros: '))
km = m / 1000 #kilometros
hm = m / 100 #hectometro
dam = m / 10 #decametro
dc = m * 10 #decimetro
cm = m * 100 #centimetro
mm = m * 1000 #milimetro
print('Valor em quilômetros: {} km \nValor em Hectômetros: {} hm \nValor em Decâmetros: {} dam \nValor em Decímetros: {:.2f} dc \nValor em Centímetros: {:.2f} cm \nValor em Milímetros: {:.2f} mm'.format(km, hm, dam, dc, cm, mm))


