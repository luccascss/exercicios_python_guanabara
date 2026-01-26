# filtro de categoria por idade
from datetime import date
ano_nascimento = int(input('Digite seu ano de nascimento para saber a sua categoria, de acordo com a idade: '))
ano_atual = date.today().year
ano_idade = (ano_atual - ano_nascimento)
if ano_idade <= 0 or ano_idade > 100:
    print('Digite valores válidos.')
elif ano_idade <= 9:
    print('Com {} anos, sua categoria atual é MIRIM!'.format(ano_idade))
elif ano_idade <= 14:
    print('Com {} amos, sua categoria atual é INFANTIL'.format(ano_idade))
elif ano_idade <= 19:
    print('Com {} anos, sua categoria atual é JUNIOR'.format(ano_idade))
elif ano_idade <= 25:
    print('Com {} anos, sua categoria atual é SÊNIOR'.format(ano_idade))
elif ano_idade > 25:
    print('Com {} anos, sua categoria atual é MASTER'.format(ano_idade))

