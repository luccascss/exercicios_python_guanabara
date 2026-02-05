#tabela do campeonato brasileiro com tupla
lista_times = ('bragantino', 'palmeiras', 'mirassol', 'são paulo', 'botafogo',
               'chapecoense', 'grêmio', 'fluminense', 'bahia', 'athletico-pr',
               'vitória','flamengo', 'atlético-mg', 'internacional', 'santos',
               'remo', 'vasco', 'corinthians', 'coritiba', 'cruzeiro')
print(f'Os 5 primeiros colocados do BR-2026 são: {lista_times[0:5]}')
print('=' * 30)
print(f'Os 4 últimos colocados são: {lista_times[16:20]}')
print('=' * 30)
print(f'Os times em ordem alfabética: {sorted(lista_times)}')
print('=' * 30)
print(f'A Chapecoense está na {lista_times.index('chapecoense') + 1}ª colocação.')
