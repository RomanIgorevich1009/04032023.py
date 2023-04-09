import numpy as np
from scipy.optimize import leastsq


def objective_function(x):
    x1, x2 = x
    y = (8 - x1)^2 - (7 - x2)^2 + 3*(x2^4)
    return y


def residual(x):
    return objective_function(x)


x0 = np.array([-3, 5])
tol = 1e-4
max_iter = 50
result = leastsq(residual, x0, ftol=tol, xtol=tol, maxfev=max_iter, full_output=True)
print("Optimization Result: ", result)