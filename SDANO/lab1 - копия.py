# variant 16
from scipy.optimize import fmin_powell
def whole_function(x1, x2):
    return 18 - 20*x1 - 8*x2 + 2*pow(x1,2) + 2*pow(x2,2)


def calc_F1(x1):  # компонента градієнту 1
    return 4*x1 -20
    


def calc_F2(x2):  # компонента градієнту 2
    return 4*x2 -8


def main():
    x1, x2 = 0, 0  # початкове наближення
    eps = 0.001
    gradientF1  = calc_F1(x1)
    gradientF2  = calc_F2(x2)
    M_iter = 100
    itert = 0
    for _ in range(M_iter):  # головний цикл
        itert += 1
        if abs(gradientF1) <= eps and abs(gradientF2) <= eps:  # перевірка чи менше епсілон
            break

        x1P  = x1
        x2P  = x2

        x1 = x1 - fmin_powell(calc_F1, 0.1)*gradientF1
        x2 = x2 - fmin_powell(calc_F2, 0.1)*gradientF2

        gradientF1 = calc_F1(x1)
        gradientF2 = calc_F2(x2)

        if x1P and x2P:
            if abs(x1-x1P)/abs(x1P) <= eps and abs(x2-x2P)/abs(x2P) <= eps: # перевірка чи менше епсілон
                break

    print("Iterations:{}, x1 = {}, x2 = {}, func = {}".format(
        itert, x1, x2, whole_function(x1, x2)))


if __name__ == "__main__":
    main()

