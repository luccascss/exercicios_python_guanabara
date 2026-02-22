# Salve dados (nome, gols, total de gols) num dicionário e número de gols dentro de uma lista
dados_jogador = dict()
gol_jogador = list()
dados_jogador['nome'] = str(input('Nome: ')).strip().upper()
partidas = int(input(f'Quantos partidas {dados_jogador['nome']} jogou? '))
for jogo in range(1, partidas + 1):
    gol = int(input(f'Quantos gols no {jogo}° jogo? '))
    gol_jogador.append(gol)
dados_jogador['gols'] = gol_jogador
dados_jogador['total_gols'] = sum(gol_jogador)
print(dados_jogador)
for k, v in dados_jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print(f'O {dados_jogador['nome']} jogou {partidas} partidas.')
for i, g in enumerate(gol_jogador):
    print(f'-> Na partida {i + 1}, fez {g}.')

