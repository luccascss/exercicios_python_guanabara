ano = int(input('Digite um ano para saber se ele é bissexto ou não: '))
ano_cond_rest_4 = ano % 4
ano_cond_rest_100 = ano % 100
ano_cond_rest_400 = ano % 400
if ano <= 1582:
    print('O ano informado deve ser maior que 1582, o primeiro ano do calendário gregoriano.')
elif ano_cond_rest_4 == 0 and ano_cond_rest_100 != 0 or ano_cond_rest_400 == 0:
   print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é um ano bissexto'.format(ano))





