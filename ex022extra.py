nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com todas as letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsuclas é {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome) - (nome.count(" "))))
#print('Seu primeiro possui {} letras'.format(nome.find(" ")))
nome_lista = nome.split()
print('Seu primeiro nome é {} e ele possui {} letras.'.format(nome_lista[0], len(nome_lista[0])))


