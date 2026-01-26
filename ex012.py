p1 = float(input('Preco do produto: R$ '))
p2 = (p1 * 5 / 100) #valor do desconto
pf = (p1 - p2) #preco final
print('Preco final: R$ {:.2f}'.format(pf))


