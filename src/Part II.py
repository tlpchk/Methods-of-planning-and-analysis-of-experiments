import numpy as np
from scipy.stats import t, norm, chi2


def t3():
    print('# 3')
    X = [435, 533, 393, 458, 525, 481, 324, 437, 348, 503, 383, 395, 416, 553, 500, 488]
    sigma = 70
    alpha = 0.01

    x_m = np.mean(X)
    n = len(X)

    N = norm(0, 1)
    L = x_m - N.ppf(1 - alpha / 2) * sigma / np.sqrt(n)
    P = x_m + N.ppf(1 - alpha / 2) * sigma / np.sqrt(n)
    print(f'[L,P] = [{x_m} - {N.ppf(1 - alpha / 2)} * {sigma} / {np.sqrt(n)},'
          f' {x_m} + {N.ppf(1 - alpha / 2)} * {sigma} / {np.sqrt(n)}] = [{L},{P}]')


def t4():
    print('# 4')
    X = np.array([383, 284, 339, 340, 305, 386, 378, 335, 344, 346])
    alpha1 = 0.1
    alpha2 = 0.05

    x_m = np.mean(X)
    n = len(X)
    S = np.sqrt(1 / (n - 1) * np.sum((X - x_m) ** 2))

    L1 = x_m - t.ppf(1 - alpha1 / 2, n - 1) * S / np.sqrt(n)
    P1 = x_m + t.ppf(1 - alpha1 / 2, n - 1) * S / np.sqrt(n)
    print(f'1-a = {1 - alpha1} => '
          f'[L,P] = [{x_m} - {t.ppf(1 - alpha1 / 2, n - 1)} * {S} / {np.sqrt(n)},'
          f' {x_m} + {t.ppf(1 - alpha1 / 2, n - 1)} * {S} / {np.sqrt(n)}] = [{L1},{P1}]')

    L2 = x_m - t.ppf(1 - alpha2 / 2, n - 1) * S / np.sqrt(n)
    P2 = x_m + t.ppf(1 - alpha2 / 2, n - 1) * S / np.sqrt(n)
    print(f'1-a = {1 - alpha2} => '
          f'[L,P] = [{x_m} - {t.ppf(1 - alpha2 / 2, n - 1)} * {S} / {np.sqrt(n)},'
          f' {x_m} + {t.ppf(1 - alpha2 / 2, n - 1)} * {S} / {np.sqrt(n)}] = [{L2},{P2}]')


def t5():
    print('# 5')
    alpha = 0.05

    x_m = 280
    n = 200
    S = 160

    L = x_m - norm.ppf(1 - alpha / 2) * S / np.sqrt(n)
    P = x_m + norm.ppf(1 - alpha / 2) * S / np.sqrt(n)
    print(f'[L,P] = [280 - 1.96 * 160 / 14.14, 280 + 1.96 * 160 / 14.14] = [{L}, {P}]')


def t7():
    print('# 7')

    a = 0.1
    x_m = 20.2
    n = 10
    S2 = 0.96

    L = (n - 1) * S2 / chi2.ppf(1 - a / 2, n - 1)
    P = (n - 1) * S2 / chi2.ppf(a / 2, n - 1)
    print(f'[L,P] = [{n - 1} * {S2} / {chi2.ppf(1 - a / 2, n - 1)},'
          f' {n - 1} * {S2} / {chi2.ppf(a / 2, n - 1)}] = [{L},{P}]')


def t8():
    print('# 8')
    X = [102, 105, 102, 100, 108, 97, 96, 98, 100, 101]
    a = 0.05

    x_m = np.mean(X)
    n = len(X)
    S = np.sqrt(1 / (n - 1) * np.sum((X - x_m) ** 2))

    L = np.sqrt((n - 1) * S ** 2 / chi2.ppf(1 - a / 2, n - 1))
    P = np.sqrt((n - 1) * S ** 2 / chi2.ppf(a / 2, n - 1))
    print(f'[L,P] = [sqrt({n - 1} * {S ** 2} / {chi2.ppf(1 - a / 2, n - 1)}),'
          f' sqrt({n - 1} * {S ** 2} / {chi2.ppf(a / 2, n - 1)})] = [{L},{P}]')


t3()
t4()
t5()
t7()
t8()
