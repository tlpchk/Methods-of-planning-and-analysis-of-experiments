import numpy as np
from scipy.stats import t


def t1():
    print('1')


def t2():
    print('2')
    n = 6
    alfa = 0.01
    m = 21.5
    X = np.array([19, 18, 22, 20, 16, 25])
    X_m = X.mean()
    S = 0
    for X_i in X:
        S += (X_i-X_m) ** 2
    S = np.sqrt(S / (n-1))
    t_0 = (X_m - m) / (S / np.sqrt(n))
    print("t_0 = ", t_0)

    print('a)')

    t_a = t.ppf(1 - alfa/2, n-1)

    print("C = (-inf, ", -t_a, "] U [", t_a, ", inf)")
    
    if t_0 <= -t_a or t_0 >= t_a:
        print("t_0 in C => we reject H_0")
    else:
        print("t_0 not in C => we accept H_0")

    L_a = X_m - t_a * S / np.sqrt(n)
    R_a = X_m + t_a * S / np.sqrt(n)

    print("[L, P] = [", L_a, ", ", R_a, "]")

    print('b)')

    t_b = t.ppf(1 - alfa, n-1)

    print("C = (-inf, ", -t_b,"]")
    
    if t_0 <= -t_b:
        print("t_0 in C => we reject H_0")
    else:
        print("t_0 not in C => we accept H_0")
    
    R_b = X_m + t_b * S / np.sqrt(n)

    print("[-inf, P] = [-inf, ", R_b, "]")



def t3():
    print('3')
    X = np.array([24.3, 20.8, 23.7, 21.3, 17.4])
    Y = np.array([18.2, 16.9, 20.2, 16.7])
    a = 0.05

    x_m = X.mean()
    y_m = Y.mean()

    n1 = len(X)
    n2 = len(Y)

    S12 = 1 / (n1 - 1) * np.sum((X - x_m) ** 2)
    S22 = 1 / (n2 - 1) * np.sum((Y - y_m) ** 2)
    Sp = np.sqrt(((n1 - 1) * S12 + (n2 - 2) * S22) / (n1 + n2 - 2))

    T = (x_m - y_m) / (Sp * np.sqrt(1 / n1 + 1 / n2))
    t_p = t.ppf(1 - a / 2, n1 + n2 - 2)
    t_l = -t_p

    print('a)')
    print(f'H0 is ok if {T} in [{t_l}, {t_p}]')
    print(f'Is H0 ok? : {t_l < T < t_p}')

    t_p = t.ppf(1 - a, n1 + n2 - 2)
    print('b)')
    print(f'H0 is ok if {T} in [-inf, {t_p}]')
    print(f'Is H0 ok? : {T < t_p}')


def t4():
    print('4')
    X = np.array([220., 185., 270., 285., 200., 295., 255., 190., 225., 230.])
    Y = np.array([190., 175., 215., 260., 215., 195., 260., 150., 155., 175])
    a = 0.05

    D = X - Y

    d_m = D.mean()

    n = len(D)

    S = np.sqrt(1 / (n - 1) * sum((D-d_m)** 2))
    T = d_m/(S/np.sqrt(n))

    t_p = t.ppf(1 - a, n-1)

    print(f'H0 is ok if {T} smaller than {t_p}')
    print(f'Is H0 ok? : {T < t_p}')


print('__________________________________')
t1()
print('__________________________________')
t2()
print('__________________________________')
t3()
print('__________________________________')
t4()
