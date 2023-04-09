# Variant 7
#
import numpy as np
from numpy import linalg


def objective(x):
    x1, x2 = x
    return (8 - x1) ^ 2 - (7 - x2) ^ 2 + 3 * x2 ^ 4


def jacobian(x):
    x1, x2 = x
    J = np.array([[-2 * (8 - x1), 2 * (7 - x2) - 12 * x2 ^ 2], [0, 12 * x2 ^ 3]])
    return J


def hessian(x):
    x1, x2 = x
    H = np.array([[2, 0], [0, 36 * x2 ^ 2]])
    return H


def marquardt(x0, ftol=1e-4, max_iter=50):
    x = x0.copy()
    lamda = pow(10, 4)
    mu = 2
    eps = pow(10, -4)
    F = objective(x)
    J = jacobian(x)
    H = hessian(x)

    for k in range(max_iter):
        delta = np.linalg.solve(H + lamda * np.eye(2), -J.T@F)
        x_new = x + delta
        F_new = objective(x_new)
        rho = (F - F_new) / (delta.T@(lamda * delta - J.T@F))

        if rho > eps:
            x = x_new
            F = F_new
            # J = jacobian(x)
            # H = hessian(x)
            lamda = max(lamda / mu, 1e-7)

        if np.linalg.norm(delta) < ftol:
            break
        else:
            lamda = min(lamda * mu, 1e7)
        return x, F, k + 1


# initial guess
x0 = np.array([-3, 5])
# solve the problem
x_opt, f_opt, iterations = marquardt(x0)
print("Optimal solution:", x_opt)
print("Objective function value:", f_opt)
print("Number of iterations:", iterations)