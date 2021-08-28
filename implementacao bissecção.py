import numpy as np

print("Método de Bissecção")

# Definindo a função
def f(x):
    return (x*np.log10(x)) - 1

# Implementação do método numérico
def bissec(a, b, tol):
    x_m = 0
    iter = 0
    while abs(b - a) > tol:
        x_m = (a + b)/2
        iter += 1
        if f(a)*f(x_m) < 0:
            b = x_m
        else:
            a = x_m
        x_raiz = x_m
    print("\nRaiz:", x_raiz)
    print("Quantidade de iterações:", iter)
    print("b - a = ", b-a, "\n")


# Atribuição dos parâmetros
tol =  1e-4
a_inicial = 2
b_inicial = 3
x_inicial = 3


bissec(a_inicial, b_inicial, tol)



