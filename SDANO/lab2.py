# variant 16
def whole_function(x1, x2):
    return 18 - 20*x1 - 8*x2 + 2*pow(x1,2) + 2*pow(x2,2)


def calc_F1(x1):  # компонента градієнту 1
    return 4*x1 -20
    


def calc_F2(x2):  # компонента градієнту 2
    return 4*x2 -8


def main():
    x1, x2 = 0, 0  # початкове наближення
    eps = 0.001
    iter = 0
    while True:

        iter+=1

        xk1 = calc_F1(x1)
        xk2 = calc_F2(x2)

        xk1_next = x1 + (-xk1)/4
        xk2_next = x2 + (-xk2)/4

        if abs(xk1_next-x1) <= eps and abs(xk2_next-x2) <= eps:
            break

        x1+=xk1_next
        x2+=xk2_next
    
    print("x1 = {}, x2 = {}, f(xk) = {} iter = {}".format(x1, x2, whole_function(x1, x2), iter))

if __name__ == "__main__":
    main()

