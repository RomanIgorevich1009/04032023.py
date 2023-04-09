# Here is the Python program to solve
# the optimization problem using the Marquardt method


import numpy as np
from numpy.linalg import inv, det
from math import sqrt


# Функція
def func(x):
    return (8 - x[0]) ** 2 - (7 - x[1]) ** 2 + 3 * (x[1] ** 4)


# диференціювання по х1 та х2
def dfdx(x):
    return np.array([
        (2 * x[0] - 16),
        (-2 * x[1] + 12 * x[1] ** 3 + 14)
    ])


# друге диференціювання по х2
def dfdx2(x):
    return (-2) + 36 * x[1] ** 2


# корінь з суми квадратів
def criter(x):
    return sqrt(16 + ((-2) + (36 * x[1] ** 2)) ** 2)


def get_gessian(x):
    tmp1 = 2
    tmp2 = dfdx2(x)
    return np.array([[tmp1, 0], [0, tmp2]])


def get_criteria(x):
    G = get_gessian(x)
    detG = det(G)
    invG = inv(G)
    Xnext = x - ((1 / detG) * invG) @ dfdx(x)
    return criter(Xnext)


eps = pow(10, -4)  # параметр збіжності
X0 = np.array([-3, 5])
k = 1  # current iteration
M = 30  # iterations
lambda_0 = pow(10, 4)


def check_termination(k, X0):
    crt = get_criteria(X0)
    if crt < eps or k > M:
        return True
    return False


def compare_functions(f1, f2):
    return f1 > f2


while not check_termination(k, X0):
    print(f"Iteration {k}: ")
    print(f"\nXk = {X0}")
    grd = dfdx(X0)
    print(f"Gradient: {grd}")
    crt = get_criteria(X0)
    print(f"Criteriy: {crt}")

    dx = (-1) * inv(get_gessian(X0) + 1.0 * np.eye(2)) @ grd
    X = X0 + dx
    print(f"Xk+1 = {X}")

    fX = func(X)
    print(f"F(X) = {fX}")
    print('*' * 30)

    if compare_functions(fX, func(X0)):
        lambda_0 = 0.5 * lambda_0
    else:
        lambda_0 = 2 * lambda_0

    X0 = X
    k += 1

print('*' * 30)
print("\nResults: ")
print(f"{k} iterations.")
print(f"X = {X0}")
print(f"F(Xmin) = {func(X0)}")
