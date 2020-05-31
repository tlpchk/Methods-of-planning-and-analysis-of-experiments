import numpy as np
from scipy.stats import t


def t3():
    print('# 3')
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


t3()
