# variant 7
from scipy.optimize import fmin_powell
from scipy.optimize import fmin
# from scipy import optimize

def whole_function(x):
    return (8-x[1])**2 - (7-x[2])**2 + 3*(x[2]**2)


def calcF1(x[1]):  # komponent 1 gradient
    return 16 + 2*x[1]


def calcF2(x2):  # komponent 2 gradient
    return 7 - 2*x[2] + 12*(x[2]**3)


def main():
    x1 = -3
    x2 = 5
    eps = 0.01
    gradF1 = calcF1(x1)
    gradF2 = calcF2(x2)
    M_iter = 50
    K_iter = 0

    for _ in range(M_iter):  # golovnyi cycle
        K_iter += 1
        if abs(gradF1) <= eps and abs(gradF2) <= eps:  # perevirka
            break

        x1po = x1
        x2po = x2

        x1 = x1 - fmin(calcF1, 0.9)*gradF1
        x2 = x2 - fmin(calcF2, 0.9)*gradF2

        gradF1 = calcF1(x1)
        gradF2 = calcF2(x2)

        if x1po and x2po:
            if abs(x1-x1po)/abs(x1po) <= eps and abs(x2-x2po)/abs(x2po) <= eps:  #perevirka
                break

    print("Iterations:{}, x1 = {}, x2 = {}, func = {}".format(
        K_iter, x1, x2, whole_function(x1, x2)))

if __name__ == "__main__":
    main()

# end of file
