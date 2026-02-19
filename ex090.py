# armazene dados de um input em um dicionário
dados = {}
dados['nome'] = str(input('Nome: ')).strip().upper()
dados['media'] = float(input('Média do aluno: '))
if dados['media'] >= 7:
    dados['situacao'] = 'APROVADO'
else:
    dados['situacao'] = 'REPROVADO'
print(f'O aluno {dados['nome']}, com média de {dados['media']} foi: {dados['situacao']}')