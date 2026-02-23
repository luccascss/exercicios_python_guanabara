# Aprimorar o ex093 para funcionar com vários jogadores e add um sistema de aproveitamento de cada jogador
dados_temp = dict()
gol_jogador = list()
dados_jogadores = list()
cont = ''
while True:
    dados_temp['nome'] = str(input('Nome: ')).strip().upper()
    partidas = int(input(f'Quantos partidas {dados_temp['nome']} jogou? '))
    for jogo in range(1, partidas + 1):
        gol = int(input(f'Quantos gols no {jogo}° jogo? '))
        gol_jogador.append(gol)
    dados_temp['gols'] = gol_jogador[:]
    dados_temp['total_gols'] = sum(gol_jogador)
    dados_jogadores.append(dados_temp.copy())
    dados_temp.clear()
    gol_jogador.clear()
    while cont != 'S' and cont != 'N':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
        if cont != 'S' and cont != 'N':
            print('Opção inválida.')
    if cont == 'S':
        cont = ''
    if cont == 'N':
        print('Calculando...')
        break
print(f'{'Código'} {'Nome':<20} {'Gols':<50} {'Total gols':<5}')
for i, data in enumerate(dados_jogadores):
    print(f'{i + 1:>6} {data['nome']:<20} {str(data['gols'])[:45]:<50} {data['total_gols']:<5}')
while True:
    print('Escolha um jogador para ver seus dados detalhadamente.')
    lev = int(input('Digite seu código: [999 para parar] ')) - 1
    if lev == 998:
        print('Programa finalizado')
        break
    elif lev >= len(dados_jogadores) or lev < 0:
        print('Valor inválido.')
    else:
        print(f'Levantamento do jogador {dados_jogadores[lev]['nome']}:')
        for i, gols in enumerate(dados_jogadores[lev]['gols']):
            print(f'No jogo {i + 1} fez {gols} gols.')
