# função chamada escreva() que receba um texto qualquer e mostre uma msg de tamanho adaptável
def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'{txt:^{len(txt) + 4}}')
    print('~' * (len(txt) + 4))


#programa principal
txt = str(input('Digite seu texto: '))
escreva(txt)
