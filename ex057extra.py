#ler o sexo de uma pessoa e insistir até que os valores sejam 'M' ou 'F'
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados inválidos! Tente novamente [M/F]: ')).strip().upper()
if sexo == 'F':
    sexo = 'FEMININO'
elif sexo == 'M':
    sexo = 'MASCULINO'
print(f'Você selecionou o sexo {sexo}')
