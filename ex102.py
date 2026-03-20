# crie função fatorial() que receba 2 parâmetros: o primeiro que indique o número a calcular e outro chamado "show" que será um valor lógico opcional indicando se será mostrado ou não o processo de cálculo.
def fatorial(num, show=False):
    n = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        n *= c
    return n


print(fatorial(5, False))