from scipy.optimize import fmin_powell
import numpy as np

def whole_function(X):
    x1=X[1-1]
    x2=X[2-1]
    y=(8-x1)**2 - (7-x2)**2 + 3*(x2**4)
    return y

def calc_F1(X):  # komponent 1 gradient
    x1=X[1-1]
    x2=X[2-1]
    return 2*x1 - 16


def calc_F2(X):  # komponent 2 gradient
    x1=X[1-1]
    x2=X[2-1]
    return - 2*x2 + 12*(x2**3) + 14

    

def FindMin(alfa):
    x1_1=x1-alfa*gradF1
    x2_1=x2-alfa*gradF2
    X1=[x1_1,x2_1]
    return whole_function(X1)

  
def fCompareX(X0, X1, eps):
    b=0
    for i in range(1, len(X0)+1):
        if abs(X1[i-1]-X0[i-1])>eps:
            b=1
    if b==0:
        v=1
    else:
        v=0
    return v



x1 = -3
x2 = 5
#
IniGuess=np.array([x1, x2])
#
eps1 = 0.001
eps2 = 0.001
alfa_0=0.5
M_iter = 100
K_iter = 0
Xprev=[x1, x2]
contin=1
while contin==1:
    K_iter+=1
    gradF1=calc_F1(Xprev)
    gradF2=calc_F2(Xprev)
    print("iter ",K_iter)#, "P=",P)
    alfa=fmin_powell(FindMin, alfa_0)
    x1_new=x1-alfa*gradF1
    x2_new=x2-alfa*gradF2
    Xnext= [x1_new,x2_new]
    x1=Xnext[1-1]
    x2=Xnext[2-1]
    print("Iterations:{}, x1 = {}, x2 = {}, alfa = {}, func = {}".format(
    K_iter, x1, x2, alfa, whole_function(Xnext)))
    if abs(whole_function(Xnext))<eps1 or fCompareX(Xprev, Xnext, eps2)==1 or K_iter>=M_iter:
        break
    Xprev=Xnext
print('\n\nChecking:\n')
result=fmin_powell(whole_function, IniGuess)
print(result)


        
