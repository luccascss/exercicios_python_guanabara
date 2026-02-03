#programa com vários inputs e leia quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem mais de 20 anos
contador_idade = 0
contador_sexo = 0
contador_f_20 = 0
while True:
    while True:
        print('===== CADASTRO DE PESSOAS ======')
        idade = int(input('Qual a sua idade? '))
        if idade < 0 or idade > 120:
            print('-' * 30)
            print('Digite um valor válido...')
            print('-' * 30)
        else:
            break
    while True:
        sexo = str(input('Qual o seu sexo? [F/M] ')).strip().upper()
        if sexo != 'M' and sexo != 'F':
            print('-' * 30)
            print('Escolha [ F ] para feminino')
            print('Escolha [ M ] para masculino')
            print('-' * 30)
        else:
            break
    if idade >= 18:
        contador_idade = contador_idade + 1
    if sexo == 'M':
        contador_sexo = contador_sexo + 1
    if sexo == 'F' and idade <= 20:
        contador_f_20 = contador_f_20 + 1
    while True:
        add_input = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if add_input != 'S' and add_input != "N":
            print('Escolha [ S ] para continuar')
            print('Escolha [ N ] para parar')
        else:
            break
    if add_input == 'S':
        print('-' * 30)
        print('Recomeçando questionário...')
        print('-' * 30)
    if add_input == 'N':
        break
print(f'Ao todo, {contador_idade} pessoas tem 18 anos ou mais.')
print(f'Temos {contador_sexo} homens cadastrados.')
print(f'Temos {contador_f_20} mulheres com 20 anos ou menos cadastradas.')