# crie função fatorial() que receba 2 parâmetros: o primeiro que indique o número a calcular e outro chamado "show" que será um valor lógico opcional indicando se será mostrado ou não o processo de cálculo.
def fatorial(num, show=0):
    n = num
    for c in range(num - 1, 1, -1):
        n *= c
    return n



fatorial(3)