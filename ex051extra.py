#PA considerando o primeiro termo e a razão por input
print('Digite a seguir o primeiro termo e a razão para descobrir os 10 primeiros termos dessa PA!')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n_do_termo = primeiro_termo + (10 - 1) * razao
for pa in range(primeiro_termo, n_do_termo + razao, razao):
    print('{}'.format(pa), end=' → ')
print('FIM')