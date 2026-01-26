# analise QUATRO pessoas e diga a média de idade do grupo, qual homem é o mais velho e quantas mulheres tem menos de 20 anos
soma_idade = 0 #soma de todas as idades para cáculo da média
nome_homem_velho = '' #nome do homem com maior idade
maior_idade_homem = 0 #maior idade entre os homens
idade_mulher = 0 #soma número de mulheres com menos de 20 anos
print('Responda o questionário a seguir e obtenha informações a cerca da média de idade, etc.')
for p in range(1, 5):
    print('===== {}ª PESSOA ====='.format(p))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: ')).__abs__()
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade = soma_idade + idade
    if p == 1 and sexo == 'M':
        nome_homem_velho = nome
        maior_idade_homem = idade
    elif idade > maior_idade_homem and sexo == 'M':
        nome_homem_velho = nome
        maior_idade_homem = idade
    elif idade < 20 and 'F' in sexo:
        idade_mulher = idade_mulher + 1
print('A média de idade do grupo é de {:.2f}'.format(soma_idade / 4))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maior_idade_homem, nome_homem_velho))
print('E {} mulheres tem menos de 20 anos'.format(idade_mulher))
