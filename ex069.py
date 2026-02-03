#programa com vários inputs e leia quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem mais de 20 anos
contador_idade = 0
contador_sexo = 0
contador_f_20 = 0
# add_input = ''
while True:
    while True:
        idade = int(input('Qual a sua idade? '))
        if idade < 0 or idade > 120:
            print('Digite um valor válido...')
        else:
            print('Validado')
            break
    while True:
        sexo = str(input('Qual o seu sexo? [F/M] ')).strip().upper()
        if sexo != 'M' and sexo != 'F':
            print('Escolha [ F ] para feminino')
            print('Escolha [ M ] para masculino')
        else:
            print('Validado')
            break
    if idade > 18:
        contador_idade = contador_idade + 1
    if sexo == 'M':
        contador_sexo = contador_sexo + 1
    if sexo == 'F' and idade < 20:
        contador_f_20 = contador_f_20 + 1
    while True:
        add_input = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if add_input != 'S' and add_input != "N":
            print('Escolha [ S ] para continuar')
            print('Escolha [ N ] para parar')
        else:
            break
    if add_input == 'S':
        print('Recomeçando questionário...')
    if add_input == 'N':
        break
print(f'{contador_idade} pessoas tem mais de 18 anos.')
print(f'{contador_sexo} homens foram cadastrados.')
print(f'{contador_f_20} mulheres com menos de 20 anos foram cadastradas.')