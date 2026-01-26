nome = str(input('Digite seu nome completo: ')).strip()
nome_lista = nome.split()
print('Primeiro nome: {}'.format(nome_lista[0].capitalize()))
print('Último nome: {}'.format(nome_lista[-1].capitalize()))

