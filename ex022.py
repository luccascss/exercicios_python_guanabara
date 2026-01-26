nome = str(input('Digite seu nome completo: ')).strip()
nomelista = nome.split()
nome0espaco = ''.join(nomelista)
print('Seu nome em letras MAIÚSCULAS é: {}'.format(nome.upper())) #nome em caps
print('Seu nome em letras MINÚSCULAS é: {}'.format(nome.lower())) #nome sem caps
print('Seu nome possui {} letras ao todo'.format(len(nome0espaco))) #n de letras sem espacos
print('Seu primeiro nome possui {} letras'.format(len(nomelista[0]))) #n de letras do primeiro nome

