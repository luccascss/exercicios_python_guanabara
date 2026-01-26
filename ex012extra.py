preco = float(input('Valor do produto sem desconto: R$ '))
#print('O valor final com o desconto de 5% é de: R$ {:.2f}'.format(preco - (preco * 5/100)))
vf = preco - (preco * 5 / 100) #valor final com desconto
print('O valor com o desconto de 5% é de: R$ {:.2f}'.format(vf))

