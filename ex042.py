# complemento do exercício 35, adicionando os tipos de triângulo equilátero, isósceles e escaleno
reta_um = float(input('Comprimento da primeira reta em centímetros: ')).__abs__()
reta_dois = float(input('Comprimento da segunda reta em centímetros: ')).__abs__()
reta_tres = float(input('Comprimento da terceira reta em centímetros: ')).__abs__()
if reta_um + reta_dois > reta_tres and reta_dois + reta_tres > reta_um and reta_tres + reta_um > reta_dois:
    print('As retas {}cm, {}cm e {}cm formam um triângulo'.format(reta_um, reta_dois, reta_tres), end= ' ')
    if reta_um == reta_dois and reta_tres == reta_um and reta_dois == reta_tres:
        print('Equilátero')
    elif reta_um != reta_dois and reta_um != reta_tres and reta_tres != reta_dois:
        print('Escaleno')
    elif reta_um == reta_dois and reta_um != reta_tres or reta_um == reta_tres and reta_um != reta_dois or reta_dois == reta_tres != reta_um:
        print('Isósceles')
else:
    print('As retas {}cm, {}cm e {}cm NÃO podem formar um triângulo'.format(reta_um, reta_dois, reta_tres))

