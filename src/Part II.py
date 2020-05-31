import numpy as np
from scipy.stats import t, norm


def t3():
    print('3')
    X = [435, 533, 393, 458, 525, 481, 324, 437, 348, 503, 383, 395, 416, 553, 500, 488]
    sigma = 70
    alpha = 0.01

    x_m = np.mean(X)
    n = len(X)

    N = norm(0, 1)
    L = x_m - N.ppf(1 - alpha / 2) * sigma / np.sqrt(n)
    P = x_m + N.ppf(1 - alpha / 2) * sigma / np.sqrt(n)
    print(f'[{L},{P}]')


def t4():
    print('4')
    X = np.array([383, 284, 339, 340, 305, 386, 378, 335, 344, 346])
    alpha1 = 0.1
    alpha2 = 0.05

    x_m = np.mean(X)
    n = len(X)
    S = np.sqrt(1 / (n - 1) * np.sum((X - x_m) ** 2))

    L1 = x_m - t.ppf(1 - alpha1 / 2, n - 1) * S / np.sqrt(n)
    P1 = x_m + t.ppf(1 - alpha1 / 2, n - 1) * S / np.sqrt(n)
    print(f'1-a = {1 - alpha1} => [L,P] = [{L1},{P1}]')

    L2 = x_m - t.ppf(1 - alpha2 / 2, n - 1) * S / np.sqrt(n)
    P2 = x_m + t.ppf(1 - alpha2 / 2, n - 1) * S / np.sqrt(n)
    print(f'1-a = {1 - alpha2} => [L,P] = [{L2},{P2}]')


t3()
t4()
