from random import sample
print('O programa a seguir definirá a ordem de apresentação dos seguintes 04 alunos: ')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
print('A ordem de apresentação é: {}'.format(sample([a1, a2, a3, a4], k=4)))

