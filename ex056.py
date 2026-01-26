#desafio idade, nome e sexo
lista_idade = []
lista_nome = []
lista_sexo = []
soma = 0
for q in range(2):
    nome = str(input('Digite seu primeiro nome: ')).lower().strip()
    lista_nome.append(nome)
    idade = int(input('Digite sua idade: '))
    lista_idade.append(idade)
    sexo = str(input('Digite [ 1 ] para MASCULINO ou [ 2 ] para FEMININO: ')).replace('1', 'm').replace('2', 'f')
    lista_sexo.append(sexo)
for l_i in lista_idade:
    soma += l_i
print('O grupo analisado possui uma média de idade de {} anos'.format(soma / 4))



