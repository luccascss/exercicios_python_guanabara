#dez primeiros termos de uma PA
primeiro_termo = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razão: '))
termo = 10
enesimo_termo = primeiro_termo - razao
print(f'A PA escolhida é: (',end='')
while termo > 0:
    termo = termo - 1
    enesimo_termo = enesimo_termo + razao
    print(f'{enesimo_termo}', end= '')
    print(')' if termo < 1 else ', ', end= '')
