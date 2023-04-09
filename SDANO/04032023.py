import numpy as nmp
from numpy import linalg as la
from math import sqrt


# Функція
def func(x):
    return ((8 - x[0]) ^ 2 - (7 - x[1]) ^ 2 + 3 * (x[1] ^ 4))

# диференціювання по х1 та х2
def dfdx(x):
    return nmp.array([
        (2 * x[0] - 16),
        (-2 * x[1] + 12 * x[1] ^ 3 + 14)
    ])

#друге диференціювання по х1
# dfdx1(x) = 2
# def dfdx1(x):
#     # return round((-6) * x[0] * x[1] * x[1] + 2, 3)
#     return round((-6) * x[0] * x[1] * x[1] + 2, 3)

#друге диференціювання по х2
def dfdx2(x):
    # return round((-2) * (x[0] ** 3) + 6 * x[1], 3)
    return ((-2) + 36 * x[1] ^ 2)


# друге диференціювання по х1 та х2
# dfdx1dx2(x) = 0
# def dfdx1dx2(x):
#     return round(36 * x[1] ** 2, 3)
#     # return round((-6) * (x[0] * x[0] * x[1]) - 9, 3)

# корінь з суми квадратів
def criter(x):
    return sqrt(16 + ((-2) + (36 * x[1] ^ 2)) ^ 2)


def get_gessian(x):
    tmp1 = 2 #dfdx1(x)
    tmp2 = dfdx2(x)
    tmp = 0 #dfdx1dx2(x)
    return nmp.array([[tmp1, tmp], [tmp, tmp2]])


def get_criteria(x):
    G = get_gessian(x)
    detG = la.det(G)
    invG = la.inv(G)
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
X0 = nmp.array([-3, 5])
k = 1  # current iteration
M = 1000  # iterations
lambda_0 = pow(10, 4)

while True:
    print(f"Iteration {k}: ")
    print(f"\nXk = {X0}")
    grd = dfdx(X0)
    print(f"Gradient: {grd}")
    crt = get_criteria(X0)
    print(f"Criteriy: {crt}")

    if check_criteria(crt) is False:
        if check_iteration(k) is False:
            # получаем шаг
            dx = ((-1) * la.inv(get_gessian(X0) + 1.0 * nmp.eye(2))).dot(grd)
            X = X0 + dx
            print(f"Xk+1 = {X}")

            fX = func(X)
            fX0 = func(X0)

            print(f"F(X) = {func(X)}")
            print('*' * 30)
            # сравнение значения функции в точках
            if compare_functions(fX, fX0):
                lambda_0 = 0.5 * lambda_0

            else:
                lambda_0 = 2 * lambda_0

            X0 = X
            k = k + 1
        else:
            break
    else:
        break

print('*' * 30)
print("\nResults: ")
print(f"{k} iterations.")
print(f"X =, {X0}")
print(f"F(Xmin) = {func(X)}")
