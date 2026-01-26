#ler o sexo de uma pessoa e insistir até que os valores sejam 'M' ou 'F'
print('Escolha a opção abaixo que represente seu sexo, sendo [M] para Masculino e [F] para Feminino: ')
sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite sua escolha: ')).upper().strip()
    if sexo == 'M' or sexo == 'F':
        if sexo == 'M':
            print('Você selecionou sexo Masculino')
        elif sexo == 'F':
            print('Você selecionou sexo Feminino')
    else:
        print('Opção inválida! Tente novamente digitando [M] para masculino ou [F] para feminino.')
print('FIM')