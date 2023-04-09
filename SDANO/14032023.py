import numpy as nmp
from numpy import linalg as LA
from math import sqrt


# Функция
def func(x):
    return (8 - x[1]) ^ 2 - (7 - x[2]) ^ 2 + 3 * x[2] ^ 4


def dfdx(x):
    return nmp.array([
        round(-2 * (8 - x[1]), 3),
        round(2 * (7 - x[2]) - 12 * x[2] ^ 2, 3)
    ])


def dfdx1(x):
    return round((-6) * x[0] * x[1] * x[1] + 2, 3)


def dfdx2(x):
    return round((-2) * (x[0] ** 3) + 6 * x[1], 3)


def dfdx1dx2(x):
    return round((-6) * (x[0] * x[0] * x[1]) - 9, 3)


def criter(x):
    return round(sqrt(
        (2 * x[0] - 3 * x[0] * x[0] * x[1] * x[1] - 9 * x[1]) ** 2
        +
        (-2 * x[0] * x[0] * x[0] * x[1] - 9 * x[0] + 3 * x[1] * x[1]) ** 2), 3)


def get_gessian(x):
    tmp1 = dfdx1(x)
    tmp2 = dfdx2(x)
    tmp = dfdx1dx2(x)
    return nmp.array([[tmp1, tmp], [tmp, tmp2]])


def get_criteria(x):
    G = get_gessian(x)
    detG = LA.det(G)
    invG = LA.inv(G)
    Xnext = x - ((1 / detG) * invG).dot(dfdx(x))
    return criter(Xnext)


def check_criteria(criteria):
    if criteria <= eps:
        return True
    return False


def check_iteration(current_iteration):
    if current_iteration > M:
        return True
    return False


def compare_functions(f1, f2):
    if f1 > f2:
        return True
    return False


eps = pow(10, -4)  # параметр сходимости
X0 = nmp.array([20, -10])
k = 1  # current iteration
M = 10_000  # iterations
l_0 = pow(10, 4)

while True:
    print(f"Iteration {k}: ")
    print(f"\nXk = {X0}")
    grd = dfdx(X0)
    print(f"Gradient: {grd}")
    crt = get_criteria(X0)
    print(f"Criteriy: {crt}")

    if check_criteria(crt) == False:
        if check_iteration(k) == False:
            # получаем шаг
            dx = ((-1) * LA.inv(get_gessian(X0) + 1.0 * nmp.eye(2))).dot(grd)
            X = X0 + dx
            print(f"Xk+1 = {X}")

            fX = func(X)
            fX0 = func(X0)

            print(f"F(X) = {func(X)}")
            print('*' * 30)
            # сравнение значения функции в точках
            if compare_functions(fX, fX0):
                l_0 = 0.5 * l_0

            else:
                l_0 = 2 * l_0

            X0 = X
            k = k + 1
        else:
            break
    else:
        break

print('*' * 30)
print("\nResults: ")
print(f"{k} iterations.")
print(f"X =", X)
print(f"F(Xmin) = {func(X)}")