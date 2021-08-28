import numpy as np

print("\nMétodo de Newton-Raphson")

# Definindo a função
def f(x):
    return (x*np.log10(x)) - 1

# Definindo a derivada
def der(x):
    dx = 1e-10
    return (f(x+dx) - f(x)) / dx

# Implementação do método numérico
def newraph(tol, x):
    x_0 = x
    dif = 1
    iter = 0
    while dif > tol:
        x_1 = x_0 - (f(x_0)/der(x_0))
        dif = abs(x_1 - x_0)
        x_0 = x_1
        iter += 1
    print("\nRaiz:", x_1)
    print("Quantidade de iterações:", iter)
    print("x_1 - x_0 = ", dif, "\n")


# Atribuição dos parâmetros
tol =  1e-4
a_inicial = 2
b_inicial = 3
x_inicial = 3


newraph(tol, x_inicial)



