# o programa a seguir analisará os valores de três retas e informará se os mesmos poderão ou não formar um triângulo. A base para construção do código é a condição de Existência: "a soma das medidas de quaisquer dois lados de um triângulo deve ser sempre maior que a medida do terceiro lado"
valor_um = float(input('Primeira medida em cm: '))
valor_dois = float(input('Segunda medida em cm: '))
valor_tres = float(input('Terceira medida em cm: '))
if valor_um < 0 or valor_dois < 0 or valor_tres < 0:
    print('Um triângulo não pode ter lados com valores negativos')
elif valor_um + valor_dois > valor_tres and valor_tres + valor_dois > valor_um and valor_um + valor_tres > valor_dois:
    print('Com os valores informados ({}cm, {}cm, {}cm), é possível formar um triângulo'.format(valor_um, valor_dois, valor_tres))
else:
    print('Com os valores informados ({}cm, {}cm, {}cm), não é possível formar um triângulo'.format(valor_um, valor_dois, valor_tres))
