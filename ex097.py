# função chamada escreva() que receba um texto qualquer e mostre uma msg de tamanho adaptável
def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'{txt:^{tam}}')
    print('~' * tam)


#programa principal
txt = str(input('Digite seu texto: '))
escreva(txt)
